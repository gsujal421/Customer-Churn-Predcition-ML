<h1 class="code-line" data-line-start=0 data-line-end=1 ><a id="CustomerChurnPredcitionML_0"></a>Customer-Churn-Predcition-ML</h1>
<p class="has-line-data" data-line-start="2" data-line-end="3">An end-to-end Machine Learning + Streamlit App project to analyze customer behavior and predict churn. The project demonstrates the complete workflow of data preprocessing, model training, and deployment with Docker.</p>
<p class="has-line-data" data-line-start="4" data-line-end="5">⚠️ Disclaimer: Predictions are for demonstration purposes only and not intended for real-world decision-making.</p>
<hr>
<h2 class="code-line" data-line-start=8 data-line-end=9 ><a id="Project_Overview_8"></a>Project Overview</h2>
<p class="has-line-data" data-line-start="10" data-line-end="11">🛠️ Built a machine learning pipeline to predict whether a customer is likely to churn.</p>
<p class="has-line-data" data-line-start="12" data-line-end="13">🔍 Includes data preprocessing, feature engineering, model selection, and hyperparameter tuning.</p>
<p class="has-line-data" data-line-start="14" data-line-end="15">🎛️ Developed an interactive Streamlit web app for predictions.</p>
<p class="has-line-data" data-line-start="16" data-line-end="17">📦 Containerized with Docker for easy deployment and reproducibility.</p>
<hr>
<h2 class="code-line" data-line-start=20 data-line-end=21 ><a id="Tech_Stack_20"></a>Tech Stack</h2>
<table class="table table-striped table-bordered">
<thead>
<tr>
<th>Category</th>
<th>Tools/Frameworks</th>
</tr>
</thead>
<tbody>
<tr>
<td>Language</td>
<td>Python 3.13</td>
</tr>
<tr>
<td>ML Libraries</td>
<td>Scikit-learn, Pandas, NumPy</td>
</tr>
<tr>
<td>Visualization</td>
<td>Matplotlib, Seaborn</td>
</tr>
<tr>
<td>UI/Deployment</td>
<td>Streamlit, Docker</td>
</tr>
</tbody>
</table>
<hr>
<h2 class="code-line" data-line-start=30 data-line-end=31 ><a id="Repository_Structure_30"></a>Repository Structure</h2>
<p class="has-line-data" data-line-start="31" data-line-end="32">tree /F &gt; structure.txt</p>
<p class="has-line-data" data-line-start="33" data-line-end="52">customer-churn-prediction/<br>
│── LICENSE<br>
│── <a href="http://README.md">README.md</a><br>
│── project-root/<br>
│   ├── requirements.txt<br>
│   └── Dockerfile<br>
│<br>
├── data/<br>
│   └── customer_churn_data.csv<br>
│<br>
├── models/<br>
│   ├── best_model.pkl<br>
│   └── scaler.pkl<br>
│<br>
├── notebooks/<br>
│   └── notebook.ipynb<br>
│<br>
└── src/<br>
└── <a href="http://app.py">app.py</a>              # Streamlit app</p>
<hr>
<h2 class="code-line" data-line-start=55 data-line-end=56 ><a id="Run_with_Docker_55"></a>Run with Docker</h2>
<p class="has-line-data" data-line-start="56" data-line-end="60">Build the Docker image<br>
docker build -t churn-app .<br>
Run the container<br>
docker run -p 8501:8501 churn-app</p>
<p class="has-line-data" data-line-start="61" data-line-end="62">Open in browser: <a href="http://localhost:8501">http://localhost:8501</a></p>
<hr>
<h2 class="code-line" data-line-start=65 data-line-end=66 ><a id="Results__Limitations_65"></a>Results &amp; Limitations</h2>
<p class="has-line-data" data-line-start="67" data-line-end="69">✅ The model achieved reasonable performance on the given dataset.<br>
⚠️ Predictions are not fully reliable due to dataset limitations.</p>
<h2 class="code-line" data-line-start=70 data-line-end=71 ><a id="Next_Steps_for_Improvement_70"></a>Next Steps for Improvement:</h2>
<p class="has-line-data" data-line-start="72" data-line-end="73">Feature engineering with domain insights.</p>
<p class="has-line-data" data-line-start="74" data-line-end="75">Expanding dataset (more balanced, diverse).</p>
<p class="has-line-data" data-line-start="76" data-line-end="77">Trying advanced models (XGBoost, LightGBM).</p>
<hr>
<h2 class="code-line" data-line-start=79 data-line-end=80 ><a id="Learning_Outcomes_79"></a>Learning Outcomes</h2>
<p class="has-line-data" data-line-start="81" data-line-end="82">Built an end-to-end ML pipeline.</p>
<p class="has-line-data" data-line-start="83" data-line-end="84">Created a Streamlit UI for interactive predictions.</p>
<p class="has-line-data" data-line-start="85" data-line-end="86">Learned Docker containerization for ML apps.</p>
<hr>
