from flask import Flask, render_template, request, jsonify
import main as solver
import json

#initial flask
app = Flask(__name__)
@app.route("/")
#homepage
def root():
    return render_template("index1.html")

#for sumbmit
@app.route("/submit",methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        c11 = request.form.get("C11")
        c12 = request.form.get("C12")
        c13 = request.form.get("C13")
        c14 = request.form.get("C14")
        c15 = request.form.get("C15")
        c16 = request.form.get("C16")
        c17 = request.form.get("C17")
        c18 = request.form.get("C18")
        c19 = request.form.get("C19")
        c21 = request.form.get("C21")
        c22 = request.form.get("C22")
        c23 = request.form.get("C23")
        c24 = request.form.get("C24")
        c25 = request.form.get("C25")
        c26 = request.form.get("C26")
        c27 = request.form.get("C27")
        c28 = request.form.get("C28")
        c29 = request.form.get("C29")
        c31 = request.form.get("C31")
        c32 = request.form.get("C32")
        c33 = request.form.get("C33")
        c34 = request.form.get("C34")
        c35 = request.form.get("C35")
        c36 = request.form.get("C36")
        c37 = request.form.get("C37")
        c38 = request.form.get("C38")
        c39 = request.form.get("C39")
        c41 = request.form.get("C41")
        c42 = request.form.get("C42")
        c43 = request.form.get("C43")
        c44 = request.form.get("C44")
        c45 = request.form.get("C45")
        c46 = request.form.get("C46")
        c47 = request.form.get("C47")
        c48 = request.form.get("C48")
        c49 = request.form.get("C49")
        c51 = request.form.get("C51")
        c52 = request.form.get("C52")
        c53 = request.form.get("C53")
        c54 = request.form.get("C54")
        c55 = request.form.get("C55")
        c56 = request.form.get("C56")
        c57 = request.form.get("C57")
        c58 = request.form.get("C58")
        c59 = request.form.get("C59")
        c61 = request.form.get("C61")
        c62 = request.form.get("C62")
        c63 = request.form.get("C63")
        c64 = request.form.get("C64")
        c65 = request.form.get("C65")
        c66 = request.form.get("C66")
        c67 = request.form.get("C67")
        c68 = request.form.get("C68")
        c69 = request.form.get("C69")
        c71 = request.form.get("C71")
        c72 = request.form.get("C72")
        c73 = request.form.get("C73")
        c74 = request.form.get("C74")
        c75 = request.form.get("C75")
        c76 = request.form.get("C76")
        c77 = request.form.get("C77")
        c78 = request.form.get("C78")
        c79 = request.form.get("C79")
        c81 = request.form.get("C81")
        c82 = request.form.get("C82")
        c83 = request.form.get("C83")
        c84 = request.form.get("C84")
        c85 = request.form.get("C85")
        c86 = request.form.get("C86")
        c87 = request.form.get("C87")
        c88 = request.form.get("C88")
        c89 = request.form.get("C89")
        c91 = request.form.get("C91")
        c92 = request.form.get("C92")
        c93 = request.form.get("C93")
        c94 = request.form.get("C94")
        c95 = request.form.get("C95")
        c96 = request.form.get("C96")
        c97 = request.form.get("C97")
        c98 = request.form.get("C98")
        c99 = request.form.get("C99")

    if request.method == "GET":
        c11 = request.args.get("C11")
        c12 = request.args.get("C12")
        c13 = request.args.get("C13")
        c14 = request.args.get("C14")
        c15 = request.args.get("C15")
        c16 = request.args.get("C16")
        c17 = request.args.get("C17")
        c18 = request.args.get("C18")
        c19 = request.args.get("C19")
        c21 = request.args.get("C21")
        c22 = request.args.get("C22")
        c23 = request.args.get("C23")
        c24 = request.args.get("C24")
        c25 = request.args.get("C25")
        c26 = request.args.get("C26")
        c27 = request.args.get("C27")
        c28 = request.args.get("C28")
        c29 = request.args.get("C29")
        c31 = request.args.get("C31")
        c32 = request.args.get("C32")
        c33 = request.args.get("C33")
        c34 = request.args.get("C34")
        c35 = request.args.get("C35")
        c36 = request.args.get("C36")
        c37 = request.args.get("C37")
        c38 = request.args.get("C38")
        c39 = request.args.get("C39")
        c41 = request.args.get("C41")
        c42 = request.args.get("C42")
        c43 = request.args.get("C43")
        c44 = request.args.get("C44")
        c45 = request.args.get("C45")
        c46 = request.args.get("C46")
        c47 = request.args.get("C47")
        c48 = request.args.get("C48")
        c49 = request.args.get("C49")
        c51 = request.args.get("C51")
        c52 = request.args.get("C52")
        c53 = request.args.get("C53")
        c54 = request.args.get("C54")
        c55 = request.args.get("C55")
        c56 = request.args.get("C56")
        c57 = request.args.get("C57")
        c58 = request.args.get("C58")
        c59 = request.args.get("C59")
        c61 = request.args.get("C61")
        c62 = request.args.get("C62")
        c63 = request.args.get("C63")
        c64 = request.args.get("C64")
        c65 = request.args.get("C65")
        c66 = request.args.get("C66")
        c67 = request.args.get("C67")
        c68 = request.args.get("C68")
        c69 = request.args.get("C69")
        c71 = request.args.get("C71")
        c72 = request.args.get("C72")
        c73 = request.args.get("C73")
        c74 = request.args.get("C74")
        c75 = request.args.get("C75")
        c76 = request.args.get("C76")
        c77 = request.args.get("C77")
        c78 = request.args.get("C78")
        c79 = request.args.get("C79")
        c81 = request.args.get("C81")
        c82 = request.args.get("C82")
        c83 = request.args.get("C83")
        c84 = request.args.get("C84")
        c85 = request.args.get("C85")
        c86 = request.args.get("C86")
        c87 = request.args.get("C87")
        c88 = request.args.get("C88")
        c89 = request.args.get("C89")
        c91 = request.args.get("C91")
        c92 = request.args.get("C92")
        c93 = request.args.get("C93")
        c94 = request.args.get("C94")
        c95 = request.args.get("C95")
        c96 = request.args.get("C96")
        c97 = request.args.get("C97")
        c98 = request.args.get("C98")
        c99 = request.args.get("C99")

    sudokuinput = [
        ['C11',c11],['C12',c12],['C13',c13],['C14',c14],['C15',c15],['C16',c16],['C17',c17],['C18',c18],['C19',c19],
        ['C21',c21],['C22',c22],['C23',c23],['C24',c24],['C25',c25],['C26',c26],['C27',c27],['C28',c28],['C29',c29],
        ['C31',c31],['C32',c32],['C33',c33],['C34',c34],['C35',c35],['C36',c36],['C37',c37],['C38',c38],['C39',c39],
        ['C41',c41],['C42',c42],['C43',c43],['C44',c44],['C45',c45],['C46',c46],['C47',c47],['C48',c48],['C49',c49],
        ['C51',c51],['C52',c52],['C53',c53],['C54',c54],['C55',c55],['C56',c56],['C57',c57],['C58',c58],['C59',c59],
        ['C61',c61],['C62',c62],['C63',c63],['C64',c64],['C65',c65],['C66',c66],['C67',c67],['C68',c68],['C69',c69],
        ['C71',c71],['C72',c72],['C73',c73],['C74',c74],['C75',c75],['C76',c76],['C77',c77],['C78',c78],['C79',c79],
        ['C81',c81],['C82',c82],['C83',c83],['C84',c84],['C85',c85],['C86',c86],['C87',c87],['C88',c88],['C89',c89],
        ['C91',c91],['C92',c92],['C93',c93],['C94',c94],['C95',c95],['C96',c96],['C97',c97],['C98',c98],['C99',c99],
    ]
    for i in sudokuinput:
        if not i[1]:
            i[1] = 0

    testpuzzle = [
        ['C11',0],['C12',0],['C13',0],['C14',0],['C15',0],['C16',6],['C17',0],['C18',8],['C19',0],
        ['C21',3],['C22',0],['C23',0],['C24',0],['C25',0],['C26',2],['C27',7],['C28',0],['C29',0],
        ['C31',7],['C32',0],['C33',5],['C34',1],['C35',0],['C36',0],['C37',6],['C38',0],['C39',0],
        ['C41',0],['C42',0],['C43',9],['C44',4],['C45',0],['C46',0],['C47',0],['C48',0],['C49',0],
        ['C51',0],['C52',8],['C53',0],['C54',0],['C55',9],['C56',0],['C57',0],['C58',2],['C59',0],
        ['C61',0],['C62',0],['C63',0],['C64',0],['C65',0],['C66',8],['C67',3],['C68',0],['C69',0],
        ['C71',0],['C72',0],['C73',4],['C74',0],['C75',0],['C76',7],['C77',8],['C78',0],['C79',5],
        ['C81',0],['C82',0],['C83',2],['C84',8],['C85',0],['C86',0],['C87',0],['C88',0],['C89',6],
        ['C91',0],['C92',5],['C93',0],['C94',9],['C95',0],['C96',0],['C97',0],['C98',0],['C99',0]]
    
    solution = solver.run(sudokuinput)#if wanna do a test can change it to testpuzzle
    return {'message':solution}
    

#run ar port 8080
app.run(port=8080)