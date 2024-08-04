import os
from PyPDF2 import PdfReader, PdfWriter

pasta = 'C:/Users/eliso/OneDrive/Área de Trabalho/leitor pdf python/separate/pdfs'

def separar_paginas(pdf_path, output_folder):
    pdf = PdfReader(pdf_path)
    total_paginas = len(pdf.pages)
    
    for i in range(total_paginas):
        writer = PdfWriter()
        writer.add_page(pdf.pages[i])
        
        output_path = os.path.join(output_folder, f'{os.path.splitext(os.path.basename(pdf_path))[0]}_pagina_{i+1}.pdf')
        with open(output_path, 'wb') as output_file:
            writer.write(output_file)
        print(f'Página {i+1} salva em: {output_path}')

    os.remove(pdf_path)
    print(f'Arquivo original removido: {pdf_path}')

for filename in os.listdir(pasta):
    if filename.lower().endswith('.pdf'):
        file_path = os.path.join(pasta, filename)
        separar_paginas(file_path, pasta)

def renomear_pdfs(pasta):

    # diretorio_script = os.path.dirname(os.path.abspath(__file__))
    # pasta = os.path.join(diretorio_script, 'pdfs')

    arquivos = [f for f in os.listdir(pasta) if f.endswith('.pdf')]
    
    arquivos.sort()

    for i, arquivo in enumerate(arquivos, start=1):
        novo_nome = f"{i}.pdf"
        caminho_antigo = os.path.join(pasta, arquivo)
        caminho_novo = os.path.join(pasta, novo_nome)
        if caminho_antigo == caminho_novo:
            print("Os Arquivos possuem o mesmo nome")
            
        else:

            os.rename(caminho_antigo, caminho_novo)
            print(f"Renomeado: {caminho_antigo} para {caminho_novo}")


renomear_pdfs(pasta)
