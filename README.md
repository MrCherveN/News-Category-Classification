<h1 style="text-align:left;">News Category Classification</h1>
<h3 style="text-align:left;">Опис проекту.</h3>

News Category Classification - проєкт з автоматичної класифікації новинних текстів за тематичними категоріями за допомогою методів обробки природної мови (NLP) та машинного навчання.

Таке рішення може використовуватися для автоматичного тегування новин, покращення пошуку, персоналізованих рекомендацій та аналітики контенту на новинних платформах.

У межах проєкту було реалізовано та порівняно три підходи:

* TF-IDF + Logistic Regression (базова модель)
* TF-IDF + SVD + XGBoost
* SentenceTransformer + Logistic Regression

Фінальною моделлю було обрано SentenceTransformer + Logistic Regression, яка показала найкращі результати на валідаційному та тестовому наборах даних.

<h3 style="text-align:left;">Бізнес-задача та мета.</h3>
Щодня новинні інтернет ресурси публікують тисячі статей, тому ручна категоризація контенту є трудомісткою та дорогою.
Мета проєкту - побудувати модель, яка автоматично визначає категорію новини за її заголовком та коротким описом.

<h3 style="text-align:left;">Дані.</h3>

Джерело: News Category Dataset на Kaggle

https://www.kaggle.com/datasets/rmisra/news-category-dataset

Файл датасету містить 209 527 записів, опубліковані у період між 2012 та 2022 роками. 

Кожен JSON-запис файла складається з таких атрибутів:
* category: Категорія, до якої належить стаття.
* headline: Заголовок статті.
* authors: Автор статті (особа, яка написала матеріал).
* link: Посилання на публікацію.
* short_description: Короткий опис (анотація) статті.
* date: Дата публікації статті.
  
<h3 style="text-align:left;">Підхід до оцінювання, обрана метрика.</h3>
Дані було розділено на:

* Train — 70%
* Validation — 15%
* Test — 15%

Для оцінювання використовувалися:
* Accuracy
* Macro F1-score
* Weighted F1-score

Основною метрикою оцінювання моделей обрано Macro F1-score, оскільки задача є багатокласовою класифікацією з незбалансованим розподілом класів. Ця метрика дозволяє оцінити якість моделі для всіх категорій незалежно від їх розміру. Інші дві метрики виступають в ролі допоміжних.

<h3 style="text-align:left;">Підхід до розв’язку та інструменти.</h3>

* очищення тексту
* видалення порожніх значень
* видалення дублікатів
* об’єднання заголовка та опису.

Було реалізовано моделі:
1. Baseline — TF-IDF + Logistic Regression
* TfidfVectorizer
* LogisticRegression
  
2. TF-IDF + SVD + XGBoost (з використанням RandomizedSearchCV)
* TfidfVectorizer
* TruncatedSVD
* XGBClassifier
* RandomizedSearchCV
  
3. SentenceTransformer + Logistic Regression
* SentenceTransformer (all-MiniLM-L6-v2)
* LogisticRegression
* Використані інструме

Використані інструменти:
* Python
* pandas
* numpy
* scikit-learn
* xgboost
* sentence-transformers
* matplotlib
* seaborn
* joblib

<h3 style="text-align:left;">Результати</h3>
Порівняння моделей (Validation)

<table>
  <thead>
    <tr>
      <th>Модель</th>
      <th>Accuracy</th>
      <th>Macro F1</th>
      <th>Weighted F1</th>
      <th>Час побудови моделі</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Baseline (TF-IDF + Logistic Regression)</b></td>
      <td>0.5921</td>
      <td>0.4345</td>
      <td>0.5634</td>
      <td>00:02:29</td>
    </tr>
    <tr>
      <td><b>TF-IDF + SVD + XGBoost</b></td>
      <td>0.4726</td>
      <td>0.2960</td>
      <td>0.4322</td>
      <td>01:21:12</td>
    </tr>
    <tr>
      <td><b>SentenceTransformer + Logistic Regression</b></td>
      <td><b>0.6118</b></td>
      <td><b>0.4763</b></td>
      <td><b>0.5911</b></td>
      <td>00:03:27</td>
    </tr>
  </tbody>
</table>

Фінальна оцінка (Test)

<table>
  <thead>
    <tr>
      <th>Accuracy</th>
      <th>Macro F1</th>
      <th>Weighted F1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>0.6094</b></td>
      <td><b>0.4782</b></td>
      <td><b>0.5902</b></td>
    </tr>
  </tbody>
</table>

<h3 style="text-align:left;">Висновки</h3>

* Найкращі результати показала модель SentenceTransformer + Logistic Regression.
* Використання семантичних ембедингів дозволило покращити якість класифікації порівняно з TF-IDF.
* Модель продемонструвала хорошу здатність до узагальнення: результати на тестовому наборі практично збігаються з результатами на валідаційному.
* Найчастіші помилки виникали між тематично близькими категоріями.


<h3 style="text-align:left;">Installation & Usage</h3>

Клонування репозиторію

git clone https://github.com/MrCherveN/News-Category-Classification.git

cd News-Category-Classification

Встановлення залежностей

pip install -r requirements.txt

Підготовка даних:
* завантажте датасет з Kaggle
* перейменуйте отриманий в "News_Category_Dataset.zip" та помістіть в папку  "data".


Запуск ноутбуків виконуйте в такому порядку:

* 01_EDA.ipynb
* 02_data_preparation.ipynb
* 03_baseline.ipynb
* 04_xgboost.ipynb
* 05_sentence_transformer.ipynb
* 06_model_comparison.ipynb
* 07_final_model_test.ipynb

<h3 style="text-align:left;">Посилання на презентацію</h3>

https://www.loom.com/share/173702e7864f40b0be89098f7dfa6362

