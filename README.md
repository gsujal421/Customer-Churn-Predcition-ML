<h1 class="code-line" data-line-start=0 data-line-end=1 ><a id="CustomerChurnPredcitionML_0"></a>Customer-Churn-Predcition-ML</h1>
<p class="has-line-data" data-line-start="2" data-line-end="3">An end-to-end Machine Learning + Streamlit App project to analyze customer behavior and predict churn. The project demonstrates the complete workflow of data preprocessing, model training, and deployment with Docker.</p>
<h2 class="code-line" data-line-start=4 data-line-end=6 ><a id="_Disclaimer_Predictions_are_for_demonstration_purposes_only_and_not_intended_for_realworld_decisionmaking_4"></a>⚠️ Disclaimer: Predictions are for demonstration purposes only and not intended for real-world decision-making.</h2>
<h2 class="code-line" data-line-start=7 data-line-end=8 ><a id="Project_Overview_7"></a>Project Overview</h2>
<p class="has-line-data" data-line-start="9" data-line-end="10">🛠️ Built a machine learning pipeline to predict whether a customer is likely to churn.</p>
<p class="has-line-data" data-line-start="11" data-line-end="12">🔍 Includes data preprocessing, feature engineering, model selection, and hyperparameter tuning.</p>
<p class="has-line-data" data-line-start="13" data-line-end="14">🎛️ Developed an interactive Streamlit web app for predictions.</p>
<p class="has-line-data" data-line-start="15" data-line-end="16">📦 Containerized with Docker for easy deployment and reproducibility.</p>
<hr>
<h2 class="code-line" data-line-start=19 data-line-end=20 ><a id="Tech_Stack_19"></a>Tech Stack</h2>
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
<h2 class="code-line" data-line-start=29 data-line-end=30 ><a id="Repository_Structure_29"></a>Repository Structure</h2>
<p class="has-line-data" data-line-start="30" data-line-end="31">tree /F &gt; structure.txt</p>
<p class="has-line-data" data-line-start="32" data-line-end="51">customer-churn-prediction/<br>
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
<h2 class="code-line" data-line-start=54 data-line-end=55 ><a id="Run_with_Docker_54"></a>Run with Docker</h2>
<p class="has-line-data" data-line-start="55" data-line-end="59">Build the Docker image<br>
docker build -t churn-app .<br>
Run the container<br>
docker run -p 8501:8501 churn-app</p>
<p class="has-line-data" data-line-start="60" data-line-end="61">Open in browser: <a href="http://localhost:8501">http://localhost:8501</a></p>
<hr>
<h2 class="code-line" data-line-start=64 data-line-end=65 ><a id="Results__Limitations_64"></a>Results &amp; Limitations</h2>
<p class="has-line-data" data-line-start="66" data-line-end="68">✅ The model achieved reasonable performance on the given dataset.<br>
⚠️ Predictions are not fully reliable due to dataset limitations.</p>
<h2 class="code-line" data-line-start=69 data-line-end=70 ><a id="Next_Steps_for_Improvement_69"></a>Next Steps for Improvement:</h2>
<p class="has-line-data" data-line-start="71" data-line-end="72">Feature engineering with domain insights.</p>
<p class="has-line-data" data-line-start="73" data-line-end="74">Expanding dataset (more balanced, diverse).</p>
<p class="has-line-data" data-line-start="75" data-line-end="76">Trying advanced models (XGBoost, LightGBM).</p>
<hr>
<h2 class="code-line" data-line-start=78 data-line-end=79 ><a id="Learning_Outcomes_78"></a>Learning Outcomes</h2>
<p class="has-line-data" data-line-start="80" data-line-end="81">Built an end-to-end ML pipeline.</p>
<p class="has-line-data" data-line-start="82" data-line-end="83">Created a Streamlit UI for interactive predictions.</p>
<p class="has-line-data" data-line-start="84" data-line-end="85">Learned Docker containerization for ML apps.</p>
<hr>
