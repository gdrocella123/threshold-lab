from flask import Flask, render_template, request
import malware_model

app = Flask(__name__, template_folder=".")
model = malware_model.MalwareModel("malware_dataset.csv")
model.train()

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")

@app.route("/threshold", methods=["GET", "POST"])
def threshold():
    threshold = float(request.args.get('t'))
    conf_matrix = model.get_confusion_matrix(threshold)

    TN = conf_matrix[0][0]
    FN = conf_matrix[1][0]
    FP = conf_matrix[0][1]
    TP = conf_matrix[1][1]

    accuracy = (TP + TN) / (TN + FN + FP + TP)

    return render_template("index.html", TN = TN, FN = FN, FP = FP, TP = TP, accuracy = accuracy)