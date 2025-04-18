# PLN

### 📦 Como começar

**1.** Clonar o repositório
```bash
git clone https://github.com/LucasOF23/PLN.git
```

**2.** Instalar as dependências via pip install
```bash
python -m venv myenv
myenv\Scripts\activate
pip install -r requirements.txt
```

## 📥 Download do modelo spaCy

Para que a lematização funcione corretamente, é necessário baixar o modelo de português do spaCy. Após instalar as dependências, execute o seguinte comando no terminal:

```bash
python -m spacy download pt_core_news_sm
```
