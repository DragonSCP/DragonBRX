from api.brx_api import BRXInfiniteAPI
import threading
import time

class BRXInfinite:
    def __init__(self):
        self.api = BRXInfiniteAPI()
        self.running = True
        
    def start_evolution_cycle(self):
        def evolution_loop():
            while self.running:
                time.sleep(3600)
                print("Ciclo de evolução executado")
        
        evolution_thread = threading.Thread(target=evolution_loop)
        evolution_thread.daemon = True
        evolution_thread.start()
    
    def chat_interface(self):
        print("BRX ∞ - Sistema Iniciado!")
        print("Digite 'status' para ver status do sistema")
        print("Digite 'sair' para encerrar")
        
        while True:
            user_input = input("\nVocê: ")
            
            if user_input.lower() == 'sair':
                self.running = False
                print("Até mais!")
                break
            elif user_input.lower() == 'status':
                status = self.api.get_system_status()
                print(f"\n{status['eternal_status']['symbolic_version']}")
                print(f"Build: {status['eternal_status']['internal_build']}")
                print(f"Melhorias: {status['eternal_status']['eternal_improvements']}")
                print(f"Ferramentas Base: {status['total_base_tools']}")
                print(f"Ferramentas Comunidade: {status['community_stats']['total_tools']}")
            else:
                result = self.api.process_request(user_input)
                print(f"\nBRX: {result['tool_results'][0]['result']['result']}")
                print(f"Qualidade: {result['quality_metrics']['final_quality']:.1%}")
                print(f"Tempo: {result['quality_metrics']['processing_time']:.2f}s")
                print(f"Ferramentas: {[tr['tool'] for tr in result['tool_results']]}")

if __name__ == "__main__":
    brx = BRXInfinite()
    brx.start_evolution_cycle()
    brx.chat_interface()
