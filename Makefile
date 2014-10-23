CONF_GRAMMAR=colino/conf/colino.ebnf
CONF_PARSER=colino/conf/parser.py

parser: ${CONF_PARSER}

${CONF_PARSER}: ${CONF_GRAMMAR}
	grako ${CONF_GRAMMAR} > ${CONF_PARSER}

tests:
	python -m unittest discover

.PHONY: tests parser
