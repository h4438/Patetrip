from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain import PromptTemplate, LLMChain

def build_prompt(inputs:list, outputs:dict, template:str, include_parser: bool = True) -> PromptTemplate:
    response_schema = [ResponseSchema(name=k, description=outputs[k])\
            for k in outputs]
    output_parser = StructuredOutputParser.from_response_schemas(response_schema)
    format_instructions = output_parser.get_format_instructions()
    if include_parser:
        prompt = PromptTemplate(template=template, input_variables=inputs,\
                          output_parser=output_parser,\
                          partial_variables={"format_instructions": format_instructions})
    else:
        prompt = PromptTemplate(template=template, input_variables=inputs,\
                          partial_variables={"format_instructions": format_instructions})
    return prompt

