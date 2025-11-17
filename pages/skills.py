from dash import register_page, html

register_page(__name__)

img_skills = 'assets/images/skills/'

data_skills = {
    "education": {
        "universidad del valle" : {
            "img": "universidad_del_valle.png",
            "title": "statistics", 
            "years": ['2020', '2023'],
            "knowledge": [
                "Fundamental Mathematics", "Calculus 1", "Calculus 2", "Calculus 3",
                "Linear Algebra", "Advanced Linear Algebra",
                "Probability Calculus 1", "Probability Calculus 2",
                "Algorithms and Programming", "Python for statistics",
                "Data Processing", "Database Management",
                "Descriptive Statistics", "Mathematical Statistics",
                "Applied Statistics", "Inferential Statistics", "Bayesian Statistics",
                "Economics for academic purposes",
                "English for academic purposes 1", "English for academic purposes 2"
            ]
        },        
        "platzi" : {
            "img": "platzi.png",
            "title": "Ciencia de datos", 
            "years": ['2023', '2024'],
            "knowledge": [
                'Introducción a la Terminal y Línea de Comandos', 
                'Profesional de Git y GitHub',
                'Fundamentos de Python', 
                'Python: Comprehensions, Funciones y Manejo de Errores', 
                'Entorno de Trabajo para Ciencia de Datos con Jupyter Notebooks y Anaconda',
                'Análisis de Negocios para Ciencia de Datos', 
                'Principios de Visualización de Datos para Business Intelligence ', 
                'Business Intelligence: Utilidad y Áreas de Oportunidad',
                'PostgreSQL Aplicado a Ciencia de Datos'
            ]
        },
        "Autodidacta" : {
            "img": "self-taught.png",
            "title": "Ciencia de datos", 
            "years": ['2023', 'actualy'],
            "knowledge": [
                'Object-Oriented Programming (OOP)',
                'Web Task Automation with Selenium',
                'Data Extraction (Web Scraping)',
                'Virtual Machine Administration in Linux',
                'Fundamentals of Machine Learning',
                'Data Visualization with Python',
                'Interactive Dashboards with Dash and Plotly',
                'Data Manipulation and Analysis with Pandas',
                'Numerical Processing with NumPy',
                'Statistical Correlation Analysis',
                'Web Development: HTML5, CSS3, and JavaScript',
                'Microsoft Excel (Data Management and Analysis)',
                'English'
            ]
        },
    },
    "tools": {}
}

# ----------------------------------------------------------------------------------------------------------------------------------
x = [data_skills['education'][element]["knowledge"] for element in data_skills["education"]]
#print(x)

education = html.Div(
    id='education_container',
    children=[
        html.Div(
            children=[
                html.P(
                    'Education',
                    className='category_skills'
                ),
            ]
        ),
        
        *[
            html.Div(
                className='education_element',
                children=[
                    html.Div(
                        className='education_col1',
                        children=[
                            html.P(
                                education_element.title(),
                                style={'font-size': '22px'}
                            ),
                            html.Img(
                                src = img_skills + data_skills["education"][education_element]["img"],
                                className='education_img'
                            ),
                            html.P(
                                data_skills["education"][education_element]['title'].title(),
                                style={'font-size': '18px'}
                            ),
                            html.P(
                                [
                                    data_skills['education'][education_element]['years'][0],
                                    ' - ',
                                    data_skills['education'][education_element]['years'][1].title()
                                ],
                                style={'font-size': '13px'}
                            )
                        ]
                    ),
                    html.Div(
                        className='education_col2',
                        children=[
                            html.Div(
                                style={'width': '100%', 'height': '100%', 'display': 'flex', 'justify-content': 'center', 'align-items': 'center',},
                                children=[
                                    html.P(
                                        'acquired knowledge: '.title(), 
                                        style={'font-size': '18px'}
                                    ),
                                ]
                            ),
                            html.Div(
                                className='education_knowledge_container',
                                children=[
                                    html.P(
                                        children='•  ' + knowledge.title(),
                                        style={ 'white-space': 'nowrap'}
                                    )
                                    for knowledge in data_skills['education'][education_element]['knowledge']
                                ]
                            )
                        ]
                    ),
                ]
            )
            for education_element in data_skills["education"]
        ],
    ]
)

layout = html.Div(
    id='skills_cotainer',
    children=[
        html.Link(rel='stylesheet', href='assets/css/skills.css'),
        education,
    ]
)