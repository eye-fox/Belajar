from flask import Flask, request, render_template_string, redirect, url_for

app = Flask(__name__)

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>XSS Lab Sederhana</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <style>
        body {
            font-family: 'Courier New', monospace;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
            color: #333;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            background: white;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        h1 {
            color: #d32f2f;
            text-align: center;
            border-bottom: 1px solid #ddd;
            padding-bottom: 10px;
        }
        .description {
            background: #fff3cd;
            border: 1px solid #ffeaa7;
            padding: 10px;
            margin-bottom: 20px;
            border-radius: 3px;
            font-size: 14px;
        }
        .input-area {
            margin-bottom: 20px;
        }
        input[type="text"] {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
            box-sizing: border-box;
        }
        button {
            background: #d32f2f;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 3px;
            cursor: pointer;
            font-family: 'Courier New', monospace;
            margin-top: 10px;
            margin-right: 10px;
        }
        button:hover {
            background: #b71c1c;
        }
        .button-reset {
            background: #6c757d;
        }
        .button-reset:hover {
            background: #545b62;
        }
        .output-area {
            margin-top: 20px;
        }
        .output-label {
            font-weight: bold;
            margin-bottom: 5px;
            display: block;
        }
        .output {
            border: 1px solid #ddd;
            padding: 15px;
            background: #f8f9fa;
            min-height: 100px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
            word-wrap: break-word;
        }
        .button-group {
            display: flex;
            gap: 10px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>XSS Lab Sederhana</h1>
        
        <div class="description">
            <strong>XSS Reflected</strong><br>
            jenis serangan di mana input berbahaya dari pengguna langsung "dipantulkan" kembali oleh website tanpa disanitasi.
        </div>
        
        <form method="POST" action="/">
            <div class="input-area">
                <label for="text">Input payload XSS:</label>
                <input type="text" id="text" name="text" placeholder="Masukkan payload XSS di sini..." value="{{ input_text }}">
                <div class="button-group">
                    <button type="submit">Test Payload</button>
                    <button type="button" class="button-reset" onclick="location.href='/'">Reset</button>
                </div>
            </div>
        </form>
        
        {% if output %}
        <div class="output-area">
            <span class="output-label">Output (dirender dengan |safe - rentan XSS):</span>
            <div class="output">
                {{ output|safe }}
            </div>
        </div>
        {% endif %}

    </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template_string(HTML_TEMPLATE, 
                                    output="", 
                                    input_text="")
    
    elif request.method == 'POST':
        input_text = request.form.get('text', '')
        output = input_text or "Tidak ada input yang diberikan"
        return render_template_string(HTML_TEMPLATE, 
                                    output=output)

if __name__ == '__main__':
    app.run(debug=True)
