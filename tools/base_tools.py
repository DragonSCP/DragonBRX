from typing import Dict, Any, List

class BaseTool:
    def __init__(self):
        self.skill_level = 0.7
        self.usage_count = 0
        
    def execute_basic(self, input_data: Any) -> Dict[str, Any]:
        self.usage_count += 1
        return {
            'result': f"Execução básica: {input_data}",
            'confidence': self.skill_level,
            'mode': 'basic'
        }
    
    def execute_advanced(self, input_data: Any) -> Dict[str, Any]:
        self.usage_count += 1
        if self.skill_level > 0.8:
            return {
                'result': f"Execução avançada: {input_data}",
                'confidence': self.skill_level,
                'mode': 'advanced'
            }
        else:
            return self.execute_basic(input_data)
    
    def improve_skill(self, improvement_factor: float):
        self.skill_level = min(1.0, self.skill_level + improvement_factor)

class ImageGenerationTool(BaseTool):
    def __init__(self):
        super().__init__()
        self.tool_name = "image_generation"
        
    def execute_basic(self, input_data: Any) -> Dict[str, Any]:
        self.usage_count += 1
        return {
            'result': f"Imagem gerada: {input_data}",
            'confidence': self.skill_level,
            'resolution': '512x512',
            'style': 'basic',
            'mode': 'basic'
        }

class TextGenerationTool(BaseTool):
    def __init__(self):
        super().__init__()
        self.tool_name = "text_generation"
        
    def execute_basic(self, input_data: Any) -> Dict[str, Any]:
        self.usage_count += 1
        return {
            'result': f"Texto gerado: {input_data}",
            'confidence': self.skill_level,
            'length': len(str(input_data)),
            'mode': 'basic'
        }

class CodeGenerationTool(BaseTool):
    def __init__(self):
        super().__init__()
        self.tool_name = "code_generation"
        
    def execute_basic(self, input_data: Any) -> Dict[str, Any]:
        self.usage_count += 1
        return {
            'result': f"Código gerado para: {input_data}",
            'confidence': self.skill_level,
            'language': 'python',
            'mode': 'basic'
        }

class WebResearchTool(BaseTool):
    def __init__(self):
        super().__init__()
        self.tool_name = "web_research"
        
    def execute_basic(self, input_data: Any) -> Dict[str, Any]:
        self.usage_count += 1
        return {
            'result': f"Pesquisa realizada: {input_data}",
            'confidence': self.skill_level,
            'sources_checked': 3,
            'mode': 'basic'
        }

class BaseToolManager:
    def __init__(self):
        self.tools = {
            'image_generation': ImageGenerationTool(),
            'text_generation': TextGenerationTool(),
            'code_generation': CodeGenerationTool(),
            'web_research': WebResearchTool()
        }
        
    def get_tool(self, tool_name: str) -> BaseTool:
        return self.tools.get(tool_name)
    
    def get_all_tools(self) -> Dict[str, BaseTool]:
        return self.tools
    
    def execute_tool(self, tool_name: str, input_data: Any) -> Dict[str, Any]:
        tool = self.get_tool(tool_name)
        if tool:
            return tool.execute_basic(input_data)
        else:
            return {'error': f"Ferramenta {tool_name} não encontrada"}
