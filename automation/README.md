\documentclass[12pt,a4paper]{report}

%---------------------------------
% Packages
%---------------------------------
\usepackage[a4paper,margin=1in]{geometry}
\usepackage{graphicx}
\usepackage[table]{xcolor}
\usepackage{titlesec}
\usepackage{setspace}
\usepackage{fancyhdr}
\usepackage{hyperref}
\usepackage{tocloft}
\usepackage{booktabs}
\usepackage{longtable}
\usepackage{array}
\usepackage{float}

%---------------------------------
% Hyperlinks
%---------------------------------
\hypersetup{
    colorlinks=true,
    linkcolor=blue,
    urlcolor=blue
}

%---------------------------------
% Line Spacing
%---------------------------------
\onehalfspacing

%---------------------------------
% Header & Footer
%---------------------------------
\setlength{\headheight}{15pt}

\pagestyle{fancy}

\fancyhf{}

\fancyhead[L]{ApexPlanet Data Analytics Internship}
\fancyhead[R]{Srinivas}

\fancyfoot[C]{\thepage}

%---------------------------------
% Document
%---------------------------------
\begin{document}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%% COVER PAGE %%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\begin{titlepage}

\centering

\vspace*{1cm}

\includegraphics[width=0.28\textwidth]{apexplanet_logo.png}

\vspace{1cm}

{\Huge\bfseries FINAL INTERNSHIP REPORT}

\vspace{0.5cm}

{\Large Data Analytics Internship}

\vspace{1cm}

\textcolor{blue}{\rule{0.8\textwidth}{1.2pt}}

\vspace{0.7cm}

{\LARGE\bfseries End-to-End Data Analytics on\\[0.3cm]
Supermarket Sales Dataset}

\vspace{0.7cm}

\textcolor{blue}{\rule{0.8\textwidth}{1.2pt}}

\vfill

\renewcommand{\arraystretch}{1.6}

\begin{tabular}{|p{5cm}|p{8cm}|}
\hline
\rowcolor{blue!15}
\textbf{Particular} & \textbf{Details} \\ \hline

Intern Name & Srinivas \\ \hline
Institute & Sreenidhi Institute of Science and Technology \\ \hline
Department & Computer Science and Engineering \\ \hline
Internship & Data Analytics Internship \\ \hline
Organization & ApexPlanet Software Pvt. Ltd. \\ \hline
Duration & 45 Days \\ \hline
Academic Year & 2026 \\ \hline

\end{tabular}

\vfill

{\large \today}

\thispagestyle{empty}

\end{titlepage}


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%% ACKNOWLEDGEMENT %%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\chapter*{Acknowledgement}

\addcontentsline{toc}{chapter}{Acknowledgement}

I would like to express my sincere gratitude to \textbf{ApexPlanet Software Pvt. Ltd.} for providing me with the opportunity to undertake this Data Analytics Internship.

This internship provided valuable hands-on experience in Data Analytics, SQL, Power BI, Statistics, Time Series Forecasting, Machine Learning, and Business Intelligence. The practical tasks helped me strengthen my analytical thinking, programming skills, and understanding of real-world business problems.

I would also like to thank the mentors and the entire ApexPlanet team for designing a structured learning program that enabled me to complete all internship tasks successfully.

Finally, I extend my gratitude to \textbf{Sreenidhi Institute of Science and Technology} for providing the academic foundation that supported my learning throughout this internship.

\vspace{1cm}

\begin{flushright}
\textbf{Srinivas}
\end{flushright}

\clearpage

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%% TABLE OF CONTENTS %%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\tableofcontents

\clearpage

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%% LIST OF FIGURES %%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\listoffigures

\clearpage

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%% LIST OF TABLES %%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\listoftables

\clearpage



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%% REPORT STARTS HERE %%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%% EXECUTIVE SUMMARY %%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\chapter{Executive Summary}

This report presents the successful completion of the \textbf{Data Analytics Internship} at \textbf{ApexPlanet Software Pvt. Ltd.} The internship focused on applying modern data analytics techniques to transform raw supermarket sales data into meaningful business insights.

Throughout the internship, the complete analytics lifecycle was implemented, beginning with data preprocessing and exploratory data analysis, followed by SQL-based business analytics, interactive dashboard development, statistical analysis, time series forecasting, customer segmentation, predictive modeling, and final reporting.

The project was carried out using industry-standard tools and technologies including Python, SQL, Power BI, Pandas, NumPy, Matplotlib, Seaborn, Statsmodels, and Scikit-learn.

The primary objective of the project was to demonstrate how data analytics can support business decision-making by identifying trends, forecasting future sales, segmenting customers, and developing predictive models.

The internship significantly strengthened practical knowledge in Data Analytics, Business Intelligence, Statistics, Machine Learning, and Python programming while providing hands-on experience with real-world business datasets.

\clearpage

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%% INTERNSHIP OBJECTIVES %%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\chapter{Internship Objectives}

The primary objectives of this internship were to understand the complete Data Analytics workflow and apply analytical techniques to solve real-world business problems using a supermarket sales dataset.

The internship focused on achieving the following objectives:

\begin{itemize}

\item Perform data cleaning and preprocessing.

\item Conduct Exploratory Data Analysis (EDA).

\item Extract business insights using SQL.

\item Develop interactive dashboards using Power BI.

\item Apply statistical analysis techniques.

\item Perform time series forecasting.

\item Segment customers using Machine Learning.

\item Develop predictive models.

\item Present analytical findings through professional reports and visualizations.

\end{itemize}

\clearpage

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%% TASKS COMPLETED %%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\chapter{Tasks Completed}

The internship was structured into five progressive tasks, each focusing on a specific stage of the data analytics lifecycle. Every task contributed toward developing a complete end-to-end analytics solution.

\section{Task 1 -- Foundational Setup and Exploratory Data Analysis}

\begin{itemize}
    \item Environment setup using Python and Jupyter Notebook.
    \item Data cleaning and preprocessing.
    \item Exploratory Data Analysis (EDA).
    \item Statistical summaries and visualizations.
    \item Identification of trends, patterns, and anomalies.
\end{itemize}

\section{Task 2 -- SQL Data Extraction}

\begin{itemize}
    \item Imported the dataset into SQLite.
    \item Executed SQL queries for business insights.
    \item Performed filtering, grouping, sorting, and aggregation.
    \item Integrated SQL with Python.
\end{itemize}

\section{Task 3 -- Dashboard Development}

\begin{itemize}
    \item Developed an interactive Power BI dashboard.
    \item Created KPI cards and business visualizations.
    \item Implemented slicers and filters.
    \item Generated business reports for decision-making.
\end{itemize}

\section{Task 4 -- Advanced Analytics}

\begin{itemize}
    \item Performed statistical analysis.
    \item Conducted time series forecasting.
    \item Applied K-Means customer segmentation.
    \item Built Linear Regression, Logistic Regression, and Decision Tree models.
\end{itemize}

\section{Task 5 -- Final Reporting}

\begin{itemize}
    \item Prepared the executive summary report.
    \item Organized project documentation.
    \item Prepared presentation materials.
    \item Finalized GitHub repositories and internship deliverables.
\end{itemize}

\clearpage

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%% PROBLEM STATEMENT %%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\chapter{Problem Statement}

Modern retail businesses generate thousands of transactions every day, resulting in large volumes of raw business data. Although this data contains valuable information, it cannot directly support decision-making without proper analysis.

Organizations require data analytics techniques to transform raw transactional data into meaningful insights that help improve business performance, customer satisfaction, inventory planning, and revenue generation.

The Supermarket Sales dataset used in this internship contains information related to customer purchases, product categories, sales transactions, payment methods, customer ratings, and branch performance. The challenge was to analyze this data and identify useful business patterns using modern data analytics techniques.

The primary goal of this internship project was to design a complete end-to-end data analytics solution capable of:

\begin{itemize}

\item Cleaning and preprocessing raw business data.

\item Performing exploratory data analysis to understand business trends.

\item Extracting meaningful insights using SQL.

\item Building interactive business dashboards using Power BI.

\item Applying statistical analysis and time series forecasting techniques.

\item Segmenting customers based on purchasing behavior.

\item Developing predictive machine learning models for business forecasting.

\item Presenting findings through a professional technical report.

\end{itemize}

The successful completion of these objectives demonstrates how modern data analytics can assist organizations in making informed, data-driven business decisions.

\clearpage

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%% DATASET OVERVIEW %%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\chapter{Dataset Overview}

The analysis conducted during this internship was based on the \textbf{Supermarket Sales Dataset}, which contains transactional records collected from supermarket branches. The dataset provides detailed information about customer purchases, product categories, payment methods, sales values, and customer ratings.

The dataset was first cleaned and preprocessed before performing exploratory analysis, visualization, statistical modeling, and machine learning.

\section{Dataset Summary}

\begin{table}[H]
\centering
\begin{tabular}{|p{6cm}|p{7cm}|}
\hline
\rowcolor{blue!15}
\textbf{Attribute} & \textbf{Value} \\ \hline

Dataset Name & Supermarket Sales Dataset \\ \hline
Number of Records & 1000 \\ \hline
Number of Features & 17 \\ \hline
Data Type & Structured Tabular Dataset \\ \hline
Source & ApexPlanet Internship Dataset \\ \hline

\end{tabular}
\caption{Dataset Summary}
\end{table}

\vspace{0.5cm}

\section{Dataset Features}

The dataset contains the following attributes:

\begin{itemize}

\item Invoice ID
\item Branch
\item City
\item Customer Type
\item Gender
\item Product Line
\item Unit Price
\item Quantity
\item Tax (5\%)
\item Sales
\item Date
\item Time
\item Payment Method
\item Cost of Goods Sold (COGS)
\item Gross Margin Percentage
\item Gross Income
\item Customer Rating

\end{itemize}

The diversity of these features enabled comprehensive business analysis, customer segmentation, sales forecasting, and predictive modeling throughout the internship.

\clearpage

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%% METHODOLOGY %%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\chapter{Methodology}

The internship followed a structured and systematic data analytics workflow to transform raw supermarket sales data into meaningful business insights. The overall methodology consisted of five major phases, beginning with data preparation and ending with professional reporting and presentation.

The workflow adopted during the internship is illustrated below:

\begin{center}
\fbox{
\parbox{0.9\textwidth}{
\centering

Data Collection

$\downarrow$

Data Cleaning \& Preprocessing

$\downarrow$

Exploratory Data Analysis (EDA)

$\downarrow$

SQL Data Extraction

$\downarrow$

Power BI Dashboard Development

$\downarrow$

Statistical Analysis

$\downarrow$

Time Series Forecasting

$\downarrow$

Customer Segmentation

$\downarrow$

Predictive Modeling

$\downarrow$

Final Report \& Presentation

}
}
\end{center}

The methodology ensured that every stage of the analytics pipeline contributed to extracting valuable business insights while maintaining data quality, analytical accuracy, and professional documentation.

\section{Phase 1 -- Data Preparation}

The dataset was imported into Python and cleaned by checking for missing values, duplicate records, and incorrect data types. The cleaned dataset formed the foundation for all subsequent analyses.

\section{Phase 2 -- Data Analysis}

Exploratory Data Analysis (EDA) and SQL queries were used to understand customer behavior, sales trends, branch performance, and product-level insights.

\section{Phase 3 -- Data Visualization}

Interactive Power BI dashboards were developed to visualize key performance indicators (KPIs), sales distribution, customer preferences, and branch-wise performance.

\section{Phase 4 -- Advanced Analytics}

Advanced statistical techniques, time series forecasting, clustering algorithms, and predictive machine learning models were implemented to generate deeper business insights.

\section{Phase 5 -- Reporting}

Finally, all analyses, visualizations, models, and findings were documented in a comprehensive technical report along with project repositories and presentation materials.

\clearpage

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%% TASK 1 %%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\chapter{Task 1: Foundational Setup and Exploratory Data Analysis}

\section{Objective}

The objective of Task 1 was to prepare the development environment, clean the dataset, understand its structure, and perform Exploratory Data Analysis (EDA) to identify trends, patterns, and business insights.

The analysis was performed using Python libraries such as Pandas, NumPy, Matplotlib, and Seaborn.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\section{Data Loading and Dataset Overview}

The dataset was imported into Python using the Pandas library. Initial inspection was performed using \texttt{head()}, \texttt{info()}, and \texttt{describe()} to understand the structure and characteristics of the dataset.

\begin{figure}[H]
\centering
\includegraphics[width=\textwidth]{assets/screenshots/task1/01_dataset_overview.png}
\caption{Dataset Overview}
\label{fig:dataset_overview}
\end{figure}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\section{Missing Value Analysis}

The dataset was checked for missing values using the \texttt{isnull().sum()} function. No significant missing values were observed, indicating that the dataset was suitable for further analysis.

\begin{figure}[H]
\centering
\includegraphics[width=\textwidth]{assets/screenshots/task1/02_missing_values.png}
\caption{Missing Value Analysis}
\label{fig:missing_values}
\end{figure}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\section{Correlation Analysis}

A correlation heatmap was generated to understand relationships among numerical variables. Strong positive correlations were observed between sales-related variables such as Quantity, Gross Income, Tax, and Total Sales.

\begin{figure}[H]
\centering
\includegraphics[width=\textwidth]{assets/screenshots/task1/03_correlation_heatmap.png}
\caption{Correlation Heatmap}
\label{fig:correlation_heatmap}
\end{figure}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\section{Sales Distribution}

Sales values were visualized using distribution plots to understand their spread and identify possible outliers. Most transactions were concentrated within a moderate sales range, while a smaller number represented high-value purchases.

\begin{figure}[H]
\centering
\includegraphics[width=\textwidth]{assets/screenshots/task1/04_sales_distribution.png}
\caption{Sales Distribution}
\label{fig:sales_distribution}
\end{figure}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\section{Product Line Analysis}

Product-wise sales analysis was performed to compare the performance of different product categories. This visualization helped identify the highest-performing product lines.

\begin{figure}[H]
\centering
\includegraphics[width=\textwidth]{assets/screenshots/task1/05_product_line_analysis.png}
\caption{Product Line Analysis}
\label{fig:product_line_analysis}
\end{figure}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\section{Key Findings}

The major observations from Task 1 are summarized below:

\begin{itemize}

\item The dataset contained 1000 transaction records.

\item Missing values were negligible after preprocessing.

\item Strong positive correlations existed among sales-related variables.

\item Product line performance varied significantly across categories.

\item Exploratory Data Analysis provided valuable business insights that guided the remaining internship tasks.

\end{itemize}

\clearpage

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%% TASK 2 %%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\chapter{Task 2: SQL Data Extraction and Python Integration}

\section{Objective}

The objective of Task 2 was to import the cleaned supermarket sales dataset into an SQLite database, execute SQL queries to extract business insights, and integrate SQL operations with Python for automated analysis.

SQLite was selected as the database management system because of its lightweight architecture and seamless integration with Python.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\section{SQLite Database Connection}

The cleaned dataset was successfully imported into an SQLite database. A database connection was established using Python's \texttt{sqlite3} library.

\begin{figure}[H]
\centering
\includegraphics[width=\textwidth]{assets/screenshots/task2/01_sql_connection.png}
\caption{Python Successfully Connected to SQLite}
\label{fig:sql_connection}
\end{figure}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\section{SQL Query Execution}

Several SQL queries were executed to analyze sales performance, branch-wise revenue, customer behavior, and payment methods.

Typical SQL operations included:

\begin{itemize}

\item SELECT

\item WHERE

\item GROUP BY

\item ORDER BY

\item Aggregate Functions

\end{itemize}

\begin{figure}[H]
\centering
\includegraphics[width=\textwidth]{assets/screenshots/task2/02_sql_query.png}
\caption{SQL Query Execution}
\label{fig:sql_query}
\end{figure}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\section{Python and SQL Integration}

Python was used to execute SQL queries directly from the SQLite database using Pandas. This enabled automated retrieval and analysis of query results.

\begin{figure}[H]
\centering
\includegraphics[width=\textwidth]{assets/screenshots/task2/03_python_sql.png}
\caption{Python and SQL Integration}
\label{fig:python_sql}
\end{figure}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\section{Business Insights}

The SQL analysis revealed important business information including:

\begin{itemize}

\item Branch-wise sales performance.

\item Revenue generated by different branches.

\item Customer purchasing behavior.

\item Product category performance.

\item Payment method distribution.

\end{itemize}

\begin{figure}[H]
\centering
\includegraphics[width=\textwidth]{assets/screenshots/task2/04_sql_results.png}
\caption{SQL Query Results}
\label{fig:sql_results}
\end{figure}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\section{Key Findings}

The major outcomes of Task 2 are summarized below:

\begin{itemize}

\item Successfully connected Python with SQLite.

\item Executed SQL queries for business analytics.

\item Automated SQL result retrieval using Python.

\item Extracted meaningful business insights through SQL analysis.

\item Prepared the processed data for visualization and dashboard development.

\end{itemize}

\clearpage

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%% TASK 3 %%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\chapter{Task 3: Interactive Dashboard and Data Visualization}

\section{Objective}

The objective of Task 3 was to transform analytical results into interactive business dashboards using Microsoft Power BI. The dashboard was designed to provide management with an intuitive overview of sales performance, customer behavior, and business trends through interactive visualizations.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\section{Dashboard Development}

An interactive Power BI dashboard was developed using the cleaned supermarket sales dataset. Multiple visual components were integrated into a single dashboard to support business decision-making.

\begin{figure}[H]
\centering
\includegraphics[width=\textwidth]{assets/screenshots/task3/01_dashboard.png}
\caption{Complete Interactive Power BI Dashboard}
\label{fig:dashboard}
\end{figure}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\section{Key Performance Indicators (KPIs)}

The dashboard includes KPI cards that summarize the most important business metrics, enabling quick assessment of overall business performance.

The KPIs include:

\begin{itemize}

\item Total Sales

\item Total Transactions

\item Average Customer Rating

\item Total Quantity Sold

\end{itemize}

\begin{figure}[H]
\centering
\includegraphics[width=\textwidth]{assets/screenshots/task3/02_kpis.png}
\caption{Key Performance Indicator (KPI) Cards}
\label{fig:kpis}
\end{figure}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\section{Business Visualizations}

Several visualizations were created to identify sales trends and compare business performance across different categories.

The dashboard includes visualizations such as:

\begin{itemize}

\item Product Line Analysis

\item Branch-wise Sales

\item City-wise Revenue

\item Payment Method Distribution

\item Customer Type Analysis

\end{itemize}

\begin{figure}[H]
\centering
\includegraphics[width=\textwidth]{assets/screenshots/task3/03_visualization.png}
\caption{Business Performance Visualization}
\label{fig:visualization}
\end{figure}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\section{Interactive Filters}

Interactive slicers and filters were implemented to allow users to dynamically explore the dataset based on different business dimensions.

The filters include:

\begin{itemize}

\item Branch

\item City

\item Product Line

\item Customer Type

\item Payment Method

\end{itemize}

\begin{figure}[H]
\centering
\includegraphics[width=\textwidth]{assets/screenshots/task3/04_filters.png}
\caption{Interactive Dashboard Filters}
\label{fig:filters}
\end{figure}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\section{Key Findings}

The dashboard successfully transformed raw sales data into meaningful business insights.

Major outcomes include:

\begin{itemize}

\item Interactive monitoring of sales performance.

\item Easy comparison of branch and city performance.

\item Identification of high-performing product lines.

\item Visualization of customer purchasing behavior.

\item Dynamic filtering for better business analysis.

\end{itemize}

\clearpage

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%% TASK 4 %%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\chapter{Task 4: Advanced Analytics and Statistical Modeling}

\section{Objective}

The objective of Task 4 was to apply advanced data analytics techniques for extracting deeper business insights using statistical analysis, time series forecasting, customer segmentation, and predictive machine learning models.

This task represents the final analytical stage of the internship where descriptive analytics was extended into predictive analytics.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\section{Monthly Sales Trend}

Monthly sales were aggregated to identify long-term business performance across different months. This visualization provides a high-level overview of sales fluctuations and seasonal business patterns.

\begin{figure}[H]
\centering
\includegraphics[width=\textwidth]{assets/screenshots/task4/01_monthly_sales.png}
\caption{Monthly Sales Trend}
\label{fig:monthly_sales}
\end{figure}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\section{Time Series Decomposition}

Time series decomposition was performed to separate the observed sales into Trend, Seasonal, and Residual components.

The decomposition revealed:

\begin{itemize}

\item Overall sales trend

\item Seasonal monthly patterns

\item Random fluctuations

\end{itemize}

\begin{figure}[H]
\centering
\includegraphics[width=\textwidth]{assets/screenshots/task4/02_decomposition.png}
\caption{Time Series Decomposition}
\label{fig:decomposition}
\end{figure}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\section{Moving Average Analysis}

A 7-day moving average was calculated to smooth short-term fluctuations and better visualize long-term sales trends.

Moving averages help reduce noise while highlighting overall business performance.

\begin{figure}[H]
\centering
\includegraphics[width=\textwidth]{assets/screenshots/task4/03_moving_average.png}
\caption{7-Day Moving Average}
\label{fig:moving_average}
\end{figure}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\section{Exponential Smoothing}

Exponential Smoothing was applied to forecast future sales while assigning greater importance to recent observations.

Compared with moving averages, exponential smoothing adapts more quickly to changing business trends.

\begin{figure}[H]
\centering
\includegraphics[width=\textwidth]{assets/screenshots/task4/04_exponential_smoothing.png}
\caption{Exponential Smoothing Forecast}
\label{fig:exp_smoothing}
\end{figure}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\section{ARIMA Forecasting}

An ARIMA(1,1,1) model was developed for forecasting future sales based on historical observations.

The forecasting model successfully captured overall sales behavior and generated short-term predictions useful for inventory planning and business decision-making.

\begin{figure}[H]
\centering
\includegraphics[width=\textwidth]{assets/screenshots/task4/05_arima_forecast.png}
\caption{ARIMA Sales Forecast}
\label{fig:arima}
\end{figure}

\clearpage

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%% TASK 4 - CUSTOMER SEGMENTATION %%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\section{Customer Segmentation using K-Means Clustering}

Customer segmentation was performed using the K-Means clustering algorithm to identify groups of customers with similar purchasing behavior.

The optimal number of clusters was determined using the Elbow Method.

\begin{figure}[H]
\centering
\includegraphics[width=\textwidth]{assets/screenshots/task4/06_elbow_method.png}
\caption{Elbow Method for Optimal Clusters}
\label{fig:elbow}
\end{figure}

After selecting the optimal number of clusters, Principal Component Analysis (PCA) was applied to visualize the customer segments in two dimensions.

\begin{figure}[H]
\centering
\includegraphics[width=\textwidth]{assets/screenshots/task4/07_customer_segmentation.png}
\caption{Customer Segmentation using PCA}
\label{fig:customer_segmentation}
\end{figure}

The clustering process identified four customer groups with different purchasing characteristics, enabling businesses to design targeted marketing strategies.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\section{Predictive Modeling}

Several machine learning algorithms were developed to predict sales and customer purchasing behavior.

The following models were implemented:

\begin{itemize}

\item Linear Regression

\item Logistic Regression

\item Decision Tree Classifier

\end{itemize}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\section{Feature Importance}

The contribution of each feature towards prediction was analyzed using feature importance analysis.

\begin{figure}[H]
\centering
\includegraphics[width=\textwidth]{assets/screenshots/task4/08_feature_importance.png}
\caption{Feature Importance Analysis}
\label{fig:feature_importance}
\end{figure}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\section{Model Performance}

The developed models achieved strong predictive performance.

The evaluation metrics obtained during experimentation are summarized below.

\begin{table}[H]
\centering
\begin{tabular}{|p{7cm}|p{5cm}|}
\hline
\rowcolor{blue!15}
\textbf{Metric} & \textbf{Result} \\ \hline

Linear Regression $R^2$ Score & 0.905 \\ \hline
Mean Absolute Error (MAE) & 58.41 \\ \hline
Root Mean Square Error (RMSE) & 78.74 \\ \hline
Logistic Regression Accuracy & 92.0\% \\ \hline
Decision Tree Accuracy & 96.5\% \\ \hline

\end{tabular}
\caption{Machine Learning Model Performance}
\end{table}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\section{Key Findings}

The major outcomes of Task 4 are summarized below:

\begin{itemize}

\item Time series forecasting successfully captured sales trends.

\item Customer segmentation identified four distinct customer groups.

\item Linear Regression achieved an $R^2$ score of 0.905.

\item Decision Tree produced the highest classification accuracy of 96.5\%.

\item Advanced analytics demonstrated the effectiveness of machine learning for business decision-making.

\end{itemize}

\clearpage

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%% TASK 5 %%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\chapter{Task 5: Final Reporting, Deployment and Presentation}

\section{Objective}

The objective of Task 5 was to professionally organize all internship deliverables, prepare technical documentation, publish project repositories, and present the complete analytics workflow in a structured and reproducible manner.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\section{Project Documentation}

Comprehensive documentation was prepared throughout the internship to ensure that every stage of the project could be understood and reproduced by other learners and professionals.

The documentation included:

\begin{itemize}

\item Project README files

\item Technical reports

\item Python notebooks

\item SQL scripts

\item Power BI dashboard

\item Machine Learning notebooks

\item GitHub repositories

\end{itemize}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\section{GitHub Repository Organization}

Each internship task was maintained in a separate GitHub repository for better project organization and version control.

The repositories include:

\begin{itemize}

\item Task 1 – Foundational Setup and EDA

\item Task 2 – SQL Data Extraction

\item Task 3 – Power BI Dashboard

\item Task 4 – Advanced Analytics and Machine Learning

\end{itemize}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\section{Project Deliverables}

The final internship submission consists of:

\begin{itemize}

\item Cleaned Dataset

\item Python Source Code

\item SQL Scripts

\item Power BI Dashboard (.pbix)

\item Machine Learning Models

\item Executive Summary Report

\item Presentation Slides

\item GitHub Repositories

\end{itemize}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\section{Skills Acquired}

Throughout the internship, the following technical skills were developed:

\begin{itemize}

\item Python Programming

\item Data Cleaning and Preprocessing

\item Exploratory Data Analysis

\item SQL Database Management

\item Power BI Dashboard Development

\item Statistical Analysis

\item Time Series Forecasting

\item Machine Learning

\item Data Visualization

\item Technical Documentation

\end{itemize}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\section{Summary}

The internship successfully demonstrated the complete Data Analytics lifecycle from raw data preprocessing to advanced predictive modeling and professional reporting.

The knowledge and practical experience gained during this internship provide a strong foundation for future work in Data Analytics, Business Intelligence, and Machine Learning.

\clearpage

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%% CONCLUSION %%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\chapter{Conclusion}

The Data Analytics Internship at \textbf{ApexPlanet Software Pvt. Ltd.} provided valuable practical exposure to the complete data analytics lifecycle. Throughout the internship, theoretical concepts learned during academic coursework were successfully applied to a real-world business dataset.

The project began with data cleaning and exploratory data analysis, followed by SQL-based business analytics, interactive dashboard development, advanced statistical analysis, time series forecasting, customer segmentation, and predictive machine learning models. Each stage contributed to transforming raw transactional data into meaningful business insights.

Interactive Power BI dashboards enabled effective visualization of business performance, while machine learning models demonstrated strong predictive capabilities. Customer segmentation further highlighted the importance of data-driven marketing and business decision-making.

The internship strengthened practical skills in Python programming, SQL, data visualization, statistical analysis, machine learning, and technical documentation. It also enhanced problem-solving abilities, analytical thinking, and the understanding of how modern organizations utilize data analytics to support strategic business decisions.

Overall, the internship successfully achieved all its objectives and provided a strong foundation for future work in Data Analytics, Business Intelligence, and Artificial Intelligence.

\clearpage

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%% FUTURE SCOPE %%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\chapter{Future Scope}

Although the project successfully demonstrated an end-to-end data analytics workflow, several opportunities exist for further improvement and expansion.

Future enhancements may include:

\begin{itemize}

\item Deployment of machine learning models as interactive web applications.

\item Integration with cloud-based databases and data warehouses.

\item Real-time sales analytics using streaming data.

\item Development of automated business intelligence dashboards.

\item Implementation of deep learning models for demand forecasting.

\item Recommendation systems for personalized customer experiences.

\item Integration with enterprise ERP and CRM platforms.

\item Automated report generation using Generative AI and Large Language Models (LLMs).

\end{itemize}

The techniques learned during this internship provide a strong foundation for developing scalable data analytics solutions capable of supporting modern business decision-making.

\clearpage

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%% REFERENCES %%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\chapter{References}

The following books, software, libraries, and online resources were referred to during the completion of this internship project.

\begin{enumerate}

\item Python Software Foundation. \textit{Python Documentation}.\\
\url{https://docs.python.org/}

\item Pandas Development Team. \textit{Pandas Documentation}.\\
\url{https://pandas.pydata.org/}

\item NumPy Developers. \textit{NumPy Documentation}.\\
\url{https://numpy.org/}

\item Matplotlib Development Team. \textit{Matplotlib Documentation}.\\
\url{https://matplotlib.org/}

\item Seaborn Documentation.\\
\url{https://seaborn.pydata.org/}

\item Scikit-learn Developers. \textit{Scikit-learn Documentation}.\\
\url{https://scikit-learn.org/}

\item Statsmodels Documentation.\\
\url{https://www.statsmodels.org/}

\item SQLite Documentation.\\
\url{https://sqlite.org/docs.html}

\item Microsoft Power BI Documentation.\\
\url{https://learn.microsoft.com/power-bi/}

\item ApexPlanet Software Pvt. Ltd. Internship Learning Materials.

\end{enumerate}

\clearpage

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%% APPENDIX %%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\chapter{Appendix}

\section{Project Repository Links}

The complete source code for each internship task has been maintained in separate GitHub repositories.

\begin{table}[H]
\centering
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{blue!15}
\textbf{Task} & \textbf{Repository} \\ \hline

Task 1 &
\url{https://github.com/Sriniccc/ApexPlanet-Task1-EDA}
\\ \hline

Task 2 &

\url{https://github.com/Sriniccc/ApexPlanet-Task2-SQL}
\\ \hline

Task 3 &

\url{https://github.com/Sriniccc/ApexPlanet-Task3-Dashboard}
\\ \hline

Task 4 &

\url{https://github.com/Sriniccc/ApexPlanet_Task4_Advanced_Analytics}

\\ \hline

\end{tabular}
\caption{GitHub Repository Links}
\end{table}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\section{Project Folder Structure}

\begin{verbatim}

ApexPlanet_Task1_Foundational_Setup_EDA
ApexPlanet_Task2_SQL_Data_Extraction
ApexPlanet_Task3_Data_Visualization
ApexPlanet_Task4_Advanced_Analytics

\end{verbatim}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\section{Software and Tools Used}

\begin{itemize}

\item Python

\item Jupyter Notebook

\item SQLite

\item Microsoft Power BI

\item Pandas

\item NumPy

\item Matplotlib

\item Seaborn

\item Statsmodels

\item Scikit-learn

\item Git

\item GitHub

\item Visual Studio Code

\item Overleaf (LaTeX)

\end{itemize}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\section{Internship Certificate}

The internship completion certificate will be attached here after successful completion of the internship.

\vspace{1cm}

\begin{center}

\fbox{
\parbox{0.8\textwidth}{
\centering

Certificate Placeholder

}
}

\end{center}

\clearpage

\end{document}