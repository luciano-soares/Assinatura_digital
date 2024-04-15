from flask import Flask, request, send_file
from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__)

@app.route('/<nome>/<departamento>/<numero>', methods=['GET'])
def index(nome, departamento, numero):
    if '@' in departamento:
        departamento = departamento.replace('@', '/')
    
    if(numero == '0'):
        i = Image.open('juntou eh junco.jpeg')
    else:
        i = Image.open('girou eh junco.jpeg')
    
    Im = ImageDraw.Draw(i)
    fonteNome         = ImageFont.truetype('Barlow-Black.ttf', 50)
    fonteDepartamento = ImageFont.truetype('Barlow-MediumItalic.ttf', 25)

    Im.text((110, 97),  nome, (250, 255, 255), font = fonteNome)
    Im.text((110, 173), departamento, (0, 0, 0), font = fonteDepartamento)

    if(numero != '0'):
        fonteTelefone = ImageFont.truetype('Barlow-MediumItalic.ttf', 37)
        Im.text((215, 270), numero, (250, 255, 255), font = fonteTelefone)

    #i.show()
    #i = i.resize((427, 141))
    i.save(nome + '.png')

    return send_file(nome+'.png', as_attachment=True)
    #return send_file(nome+'.png', mimetype='image/gif')

    #return '<h1>Welcome ' + nome + ' of departament ' + departamento + '</h1>'

if __name__ == '__main__':
    app.run(debug=True, port=5001)