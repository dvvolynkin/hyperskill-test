include .env
export

init_eval:
	npx promptfoo@latest eval -c./configs/init.yaml --output ./outputs/init.json

view:
	npx promptfoo@latest view -y
