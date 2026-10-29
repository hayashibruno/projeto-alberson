import pandas as pd
from reportlab.pdfgen import canvas

##############################################

#df = pd.ExcelFile(r"C:\Users\Master\Downloads\Projeto 4 bim - PYTHON\projeto4bi.xlsx")
df = pd.read_excel(r"C:\Users\Master\Downloads\Projeto 4 bim\Projeto 4 bim\Projeto 4 bim - PYTHON\projeto4bi.xlsx", sheet_name="Brasileirão 2026", header=2)


times = df.iloc[1:21, 0:5]
pontos = times.iloc[:, 2] * 3 + times.iloc[:, 3] * 1
times['Pontos Calculados'] = pontos

nomes = []
pontos_lista = []

#Pegar os nomes e pontos dos times

for i in range(len(times)):
    nomes.append(times.iloc[i, 0])
    pontos_lista.append(times.iloc[i, 5])

for i in range(len(pontos_lista)):
    for j in range(i+1,len(pontos_lista)):
        if pontos_lista[i] < pontos_lista[j]:
            aux = pontos_lista[i]
            pontos_lista[i] = pontos_lista[j]
            pontos_lista[j] = aux

            aux = nomes[i]
            nomes[i] = nomes[j]
            nomes[j] = aux

#Ordenar posiçoes
posicoes = []

for i in range(len(pontos_lista)):
    if i == 0:
        posicoes.append(1)
    elif pontos_lista[i] == pontos_lista[i-1]:
        posicoes.append(posicoes[i-1])
    else:
        posicoes.append(i+1)


#PDF

def gerarpdf(nomes, pontos_lista, posicoes, times):
    try:
        pdf = canvas.Canvas('Campeonato Brasileiro.pdf')

        pdf.setFillColor('black')
        pdf.setTitle('Campeonato Brasileiro 2026')

        pdf.setFont("Helvetica-Bold", 18)
        pdf.drawString(30, 800, "BRASILEIRÃO 2026")

        pdf.setFont("Helvetica", 11)
        pdf.drawString(30, 765, "Classificação do Campeonato Brasileiro")

        pdf.setFont("Helvetica-Bold", 10)
        pdf.drawString(30, 740, "Pos.")
        pdf.drawString(75, 740, "Time")
        pdf.drawString(300, 740, "Jogos")
        pdf.drawString(370, 740, "Vitórias")
        pdf.drawString(450, 740, "Empates")
        pdf.drawString(540, 740, "Derrotas")
        pdf.drawString(640, 740, "Pontos")

        y = 720

        for i in range(len(nomes)):
            for j in range(len(times)):
                if nomes[i] == times.iloc[j, 0]:
                    pdf.drawString(30, y, str(posicoes[i]))
                    pdf.drawString(75, y, str(nomes[i]))
                    pdf.drawString(300, y, str(times.iloc[j, 1]))
                    pdf.drawString(370, y, str(times.iloc[j, 2]))
                    pdf.drawString(450, y, str(times.iloc[j, 3]))
                    pdf.drawString(540, y, str(times.iloc[j, 4]))
                    pdf.drawString(640, y, str(pontos_lista[i]))

            y = y - 20
        
        pdf.save()
        print(f'Campeonato Brasileiro.pdf foi gerado com sucesso: ')
    except Exception as erro:
        print(f'Erro ao gerar o arquivo pdf: {erro}')




#HTML
arquivo_html = open("index.html", "w", encoding="utf-8")


arquivo_html.write("""
<!DOCTYPE html>
<html lang="pt-BR">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Brasileirão 2026 - Classificação</title>

    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: Arial, Helvetica, sans-serif;
            background: #07131d;
            color: #f1f5f9;
            min-height: 100vh;
        }

        header {
            background: linear-gradient(120deg, #06131d, #123443, #06131d);
            padding: 35px 20px;
            text-align: center;
        }

        header h1 {
            font-size: 38px;
            margin-bottom: 10px;
            letter-spacing: 2px;
        }

        header h1 span {
            color: #4ade80;
        }

        header p {
            color: #a9bdca;
            font-size: 14px;
            letter-spacing: 2px;
        }

        main {
            width: 94%;
            max-width: 1200px;
            margin: 35px auto;
            padding: 25px;
            background: #0a1925;
            border: 1px solid #203747;
            border-radius: 14px;
            box-shadow: 0 15px 45px rgba(0, 0, 0, 0.3);
        }

        h2 {
            font-size: 23px;
            margin-bottom: 25px;
            padding-left: 14px;
        }

        .tabela-container {
            width: 100%;
            overflow-x: auto;
            border-radius: 9px;
            border: 1px solid #233b4c;
        }

        table {
            width: 100%;
            min-width: 700px;
            border-collapse: collapse;
        }

        thead {
            background: #172b3b;
        }

        th {
            padding: 16px 12px;
            color: #a9bdca;
            font-size: 12px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        td {
            padding: 14px 12px;
            text-align: center;
            border-bottom: 1px solid #20303d;
        }

        td:nth-child(2) {
            text-align: left;
            font-weight: bold;
        }

        tbody tr {
            background: #0b1a27;
            transition: background 0.2s;
        }

        tbody tr:nth-child(even) {
            background: #102231;
        }

        tbody tr:hover {
            background: #1a3745;
        }

        tbody tr:last-child td {
            border-bottom: none;
        }

        td:last-child {
            color: #4ade80;
            font-weight: bold;
            font-size: 16px;
        }

        .botoes {
            display: flex;
            justify-content: flex-end;
            margin-top: 25px;
        }

        .botao-pdf {
            display: inline-block;
            padding: 14px 22px;
            background: linear-gradient(135deg, #4ade80, #16a34a);
            color: #052e16;
            border: none;
            border-radius: 8px;
            font-size: 14px;
            font-weight: bold;
            text-decoration: none;
            cursor: pointer;
            transition: transform 0.2s;
        }

        .botao-pdf:hover {
            transform: translateY(-2px);
        }
    </style>
</head>

<body>

    <header>
        <h1>BRASILEIRÃO <span>2026</span></h1>
        <p>Classificação do Campeonato Brasileiro</p>
    </header>

    <main>
        <h2>Tabela de Classificação</h2>

        <div class="tabela-container">
            <table>
                <thead>
                    <tr>
                        <th>Posição</th>
                        <th>Time</th>
                        <th>Jogos</th>
                        <th>Vitórias</th>
                        <th>Empates</th>
                        <th>Derrotas</th>
                        <th>Pontos</th>
                    </tr>
                </thead>

                <tbody>
""")

for i in range(len(nomes)):
    for j in range(len(times)):
        if nomes[i] == times.iloc[j, 0]:
            linha = f"""
                    <tr>
                        <td>{posicoes[i]}</td>
                        <td>{nomes[i]}</td>
                        <td>{times.iloc[j, 1]}</td>
                        <td>{times.iloc[j, 2]}</td>
                        <td>{times.iloc[j, 3]}</td>
                        <td>{times.iloc[j, 4]}</td>
                        <td>{pontos_lista[i]}</td>
                    </tr>
                    """
            arquivo_html.write(linha)

arquivo_html.write("""
                </tbody>
            </table>
        </div>

        <div class="botoes">
            <a href="Campeonato%20Brasileiro.pdf"
               target="_blank"
               class="botao-pdf">
                Abrir classificação em PDF
            </a>
        </div>
    </main>

</body>
</html>
""")

arquivo_html.close()

gerarpdf(nomes, pontos_lista, posicoes, times)

print("Arquivo HTML criado com sucesso!")
