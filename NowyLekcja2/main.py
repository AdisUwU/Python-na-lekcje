from flask import Flask
import random
app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<a href="/random_fact">Zobacz losowy fakt!</a>'

@app.route("/random_fact")
def random_fact():
    facts_list = ["Większość osób cierpiących na uzależnienie technologiczne doświadcza silnego stresu, gdy znajdują się poza zasięgiem sieci lub nie mogą korzystać ze swoich urządzeń.","Według badania przeprowadzonego w 2018 roku ponad 50% osób w wieku od 18 do 34 lat uważa się za zależne od swoich smartfonów.","Badanie zależności technologicznych jest jednym z najważniejszych obszarów współczesnych badań naukowych.","Według badania z 2019 r. ponad 60% osób odpowiada na wiadomości służbowe na swoich smartfonach w ciągu 15 minut po wyjściu z pracy.","Jednym ze sposobów walki z uzależnieniem od technologii jest poszukiwanie zajęć, które sprawiają przyjemność i poprawiają nastrój.","Elon Musk twierdzi, że sieci społecznościowe są zaprojektowane tak, aby trzymać nas na platformie, abyśmy spędzali jak najwięcej czasu na przeglądaniu treści.","Elon Musk opowiada się także za regulacją sieci społecznościowych i ochroną danych osobowych użytkowników. Twierdzi, że sieci społecznościowe gromadzą o nas ogromną ilość informacji, które następnie można wykorzystać do manipulowania naszymi myślami i zachowaniami.",]
    return f'<p>{random.choice(facts_list)}</p>' '<h></h>' '<a href="/strona_o_niczym">Tu nic nie ma naprawde!</a>'

@app.route("/strona_o_niczym")
def Strona_o_niczym():
    return '<p>muwiłem że o niczym :-)</p>'

app.run(debug=True)