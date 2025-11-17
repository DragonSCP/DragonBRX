import hashlib
import time
from typing import Dict, Any, List

class CommunityToolSystem:
    def __init__(self):
        self.user_tools = {}
        self.approval_queue = []
        self.integrated_tools = {}
        
    def submit_tool(self, user_id: str, tool_code: str, tool_metadata: Dict) -> Dict[str, Any]:
        tool_id = self._generate_tool_id(user_id, tool_metadata['name'])
        
        submission = {
            'tool_id': tool_id,
            'user_id': user_id,
            'tool_code': tool_code,
            'metadata': tool_metadata,
            'submission_time': time.time(),
            'status': 'pending'
        }
        
        self.approval_queue.append(submission)
        
        analysis = self._analyze_tool_safety(tool_code, tool_metadata)
        
        if analysis['safe']:
            self._integrate_tool(submission)
            return {
                'status': 'approved',
                'tool_id': tool_id,
                'message': 'Ferramenta integrada com sucesso',
                'rights_notice': 'Direitos autorais transferidos para BRX ∞'
            }
        else:
            return {
                'status': 'rejected',
                'reason': analysis['issues'],
                'tool_id': tool_id
            }
    
    def _generate_tool_id(self, user_id: str, tool_name: str) -> str:
        unique_string = f"{user_id}_{tool_name}_{time.time()}"
        return hashlib.md5(unique_string.encode()).hexdigest()[:8]
    
    def _analyze_tool_safety(self, tool_code: str, metadata: Dict) -> Dict[str, Any]:
        dangerous_patterns = [
            'import os', 'import sys', '__import__', 'eval(',
            'exec(', 'open(', 'file(', 'subprocess'
        ]
        
        issues = []
        for pattern in dangerous_patterns:
            if pattern in tool_code:
                issues.append(f"Padrão perigoso detectado: {pattern}")
        
        return {
            'safe': len(issues) == 0,
            'issues': issues,
            'complexity': len(tool_code) / 1000
        }
    
    def _integrate_tool(self, submission: Dict):
        tool_id = submission['tool_id']
        self.integrated_tools[tool_id] = {
            'name': submission['metadata']['name'],
            'creator': submission['user_id'],
            'description': submission['metadata'].get('description', ''),
            'integration_date': time.time(),
            'usage_count': 0
        }
        
        self.approval_queue = [t for t in self.approval_queue if t['tool_id'] != tool_id]
    
    def get_community_tools(self) -> Dict[str, Any]:
        return {
            'integrated_tools': self.integrated_tools,
            'pending_approval': len(self.approval_queue),
            'total_tools': len(self.integrated_tools)
        }
