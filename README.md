# Serverless Function HTTP Trigger Example

This example demonstrates the core concept of a serverless function (FaaS) triggered by an HTTP request. It uses a simple Python Flask application to simulate how a developer writes only the business logic, while the underlying infrastructure (like an HTTP server) is handled by a cloud provider in a real serverless environment. The function responds with a personalized greeting based on input.

## Language

`python`

## How to Run

1. Install Flask: `pip install Flask`
2. Run the application: `python main.py`
3. Access in your browser or with curl:
   - GET: `http://127.0.0.1:5000/hello?name=Kullanıcı`
   - POST: `curl -X POST -H "Content-Type: application/json" -d '{"name": "API_Kullanıcısı"}' http://127.0.0.1:5000/hello`

## Original Article

This example accompanies the Turkish article: [Serverless Mimarilerle Uygulama Geliştirme: İstediğiniz Gibi, İşte Burada!](https://fatihsoysal.com/blog/serverless-mimarilerle-uygulama-gelistirme-istediginiz-gibi-iste-burada/).

## License

MIT — see [LICENSE](LICENSE).
