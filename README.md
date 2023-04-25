# applications python3 api-flask and docker

Development of applications python api flask with json and docker. 
Create, Read, Update, Delete and Search date json

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install aplication.

```bash
pip install -r requirements
```

## Usage

```python
docker image build -t python-docker . 
docker run --publish 8000:5000 python-docker
```
## Postman

"/listar"

"/salvar"

"/atualizarItem/<id>"

"/deletar/<id>"

"/procurar/<name_city>"


## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)