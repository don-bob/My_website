from dash import register_page, html

register_page(__name__)

img_skills = 'assets/images/skills/'

data_skills = {
    "education": {
        "universidad del valle" : {
            "img": "universidad_del_valle.png",
            "title": "Estadistica", 
            "years": [2020, 2023],
            "knowledge": ['estadistica descritiva', 'estadistica inferencial', 'calculo', 'algebra', 'probabilidad']
        },        
        "platzi" : {
            "img": "platzi.png",
            "title": "Ciencia de datos", 
            "years": [2023, 2024],
            "knowledge": ['programacion']
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
                html.Hr()
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
                                data_skills["education"][education_element]['title'],
                                style={'font-size': '18px'}
                            ),
                            html.P(
                                [
                                    data_skills['education'][education_element]['years'][0],
                                    ' - ',
                                    data_skills['education'][education_element]['years'][1]
                                ],
                                style={'font-size': '14px'}
                            )
                        ]
                    ),
                    html.Div(
                        className='education_col2',
                        children=[
                            html.P(
                                'Conocimientos adquiridos'
                            ),
                            html.Div(
                                className='education_knowledge_container',
                                children=[
                                    html.P(
                                        children='- ' + knowledge.title()
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