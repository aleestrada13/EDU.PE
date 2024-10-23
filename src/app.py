from flask import Flask, url_for, redirect, request, render_template
from routes.psychology.PsychologyRoute import psychology_page
from routes.wellbeing.WellbeingRoute import wellbeing_page
from routes.selfesteem.SelfesteemRoute import selfesteem_page
from routes.social.SocialRoute import social_page
from routes.test.TestRoute import test_page


app = Flask(__name__)

# Routes
app.register_blueprint(psychology_page)
app.register_blueprint(wellbeing_page)
app.register_blueprint(selfesteem_page)
app.register_blueprint(social_page)
app.register_blueprint(test_page)

def calcular_resultado(respuestas):
    puntajes = {
        "Nunca": 0,
        "A veces": 10,
        "Siempre": 20
    }
    
    puntaje_total = sum(puntajes[respuesta] for respuesta in respuestas.values())
    
    if puntaje_total <= 70:
        return {
            "puntaje": puntaje_total,
            "mensaje": "Necesitas mejorar. Considera implementar más estrategias para manejar el estrés.",
            "nivel": "bajo"
        }
    elif puntaje_total <= 130:
        return {
            "puntaje": puntaje_total,
            "mensaje": "Estás en el camino correcto, pero hay áreas que puedes mejorar.",
            "nivel": "medio"
        }
    else:
        return {
            "puntaje": puntaje_total,
            "mensaje": "Excelente, tienes buenas prácticas para gestionar el estrés y mantener tu bienestar emocional. ¡Sigue así!",
            "nivel": "alto"
        }

@app.route("/")
def index():
    return redirect(url_for('psychology_page.Psychology'))

@app.route('/submit-test', methods=['POST'])
def submit_test():
    respuestas = {str(i): request.form.get(f'question_{i}') 
                 for i in range(1, 11)}
    
    print(respuestas)
    
    resultado = calcular_resultado(respuestas)
    
    return render_template('/pages/Resultado.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)