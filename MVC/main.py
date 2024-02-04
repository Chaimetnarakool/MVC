from flask import Flask, render_template, request
from controller import process_fine_tuning

app = Flask(__name__)

@app.route('/')
def index():
    # แสดงหน้าเว็บหลัก
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    # รับข้อมูลจากฟอร์มและประมวลผลการ Feine-Tuning
    training_data_path = request.form['training_data_path']  # รับพาธข้อมูลการฝึก
    model_path = request.form['model_path']                  # รับพาธโมเดล
    fine_tuning_method = request.form['fine_tuning_method']  # รับวิธีการ Fine-Tuning
    result = process_fine_tuning(training_data_path, model_path, fine_tuning_method)  # ประมวลผล Fine-Tuning
    return result

if __name__ == '__main__':
    # เริ่มการทำงานของเซิร์ฟเวอร์ Flask
    app.run(debug=True)
