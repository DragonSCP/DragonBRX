import time
from typing import Dict, Any

class BRXInfiniteAPI:
    def __init__(self):
        from core.infinite_versioning import InfiniteVersionSystem
        from core.deep_multilayer_thinking import DeepMultilayerThinking
        from tools.base_tools import BaseToolManager
        from tools.community_tools import CommunityToolSystem
        
        self.version_system = InfiniteVersionSystem()
        self.thinking_engine = DeepMultilayerThinking()
        self.tool_manager = BaseToolManager()
        self.community_system = CommunityToolSystem()
        self.user_sessions = {}
        
    def process_request(self, user_input: str, user_id: str = "anonymous") -> Dict[str, Any]:
        start_time = time.time()
        
        thinking_result = self.thinking_engine.process_with_deep_thinking(user_input)
        
        tools_used = thinking_result['final_result']['best_result']['tools_executed']
        tool_results = []
        
        for tool_name in tools_used:
            tool_result = self.tool_manager.execute_tool(tool_name, user_input)
            tool_results.append({
                'tool': tool_name,
                'result': tool_result
            })
        
        processing_time = time.time() - start_time
        
        self.version_system.record_eternal_improvement({
            'type': 'user_interaction',
            'significance': thinking_result['quality_achieved'],
            'description': f"Processado: {user_input[:50]}..."
        })
        
        return {
            'user_input': user_input,
            'user_id': user_id,
            'tool_results': tool_results,
            'thinking_process': thinking_result['thinking_process'],
            'quality_metrics': {
                'final_quality': thinking_result['quality_achieved'],
                'iterations': thinking_result['iterations_performed'],
                'processing_time': processing_time
            },
            'system_info': {
                'version': self.version_system.symbolic_version,
                'build': self.version_system.internal_build,
                'improvements': self.version_system.eternal_improvement_counter
            },
            'community_stats': self.community_system.get_community_tools()
        }
    
    def submit_tool(self, user_id: str, tool_code: str, tool_metadata: Dict) -> Dict[str, Any]:
        return self.community_system.submit_tool(user_id, tool_code, tool_metadata)
    
    def get_system_status(self) -> Dict[str, Any]:
        eternal_status = self.version_system.get_eternal_status()
        community_stats = self.community_system.get_community_tools()
        
        return {
            'eternal_status': eternal_status,
            'community_stats': community_stats,
            'total_base_tools': len(self.tool_manager.get_all_tools()),
            'active_sessions': len(self.user_sessions)
        }
