from flask import Flask, render_template, request
import your_image_generation_module  # あなたの画像生成モジュール

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_image():
    # ユーザーからのデータを受け取り、画像生成を実行
    user_input = request.form['input']
    generated_image_path = your_image_generation_module.generate(user_input)
    return f'<img src="{generated_image_path}" alt="Generated Image">'

if __name__ == '__main__':
    
