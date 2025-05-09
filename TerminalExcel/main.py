from switch_interface_fetcher import SwitchInterfaceStatusFetcher, salvar_todos_em_um_csv

# Lista de switches com IPs diferentes
switches = [
    SwitchInterfaceStatusFetcher("10.1.80.163", "leitura", "sbwxdr2d2"),
    SwitchInterfaceStatusFetcher("10.1.80.161", "leitura", "sbwxdr2d2"),
    SwitchInterfaceStatusFetcher("10.1.80.235", "leitura", "sbwxdr2d2"),
    SwitchInterfaceStatusFetcher("10.1.80.160", "leitura", "sbwxdr2d2"),
    SwitchInterfaceStatusFetcher("10.1.80.168", "leitura", "sbwxdr2d2"),
    # SwitchInterfaceStatusFetcher("10.1.80.158", "leitura", "sbwxdr2d2"),
    SwitchInterfaceStatusFetcher("10.1.80.180", "leitura", "sbwxdr2d2"),
    SwitchInterfaceStatusFetcher("10.1.80.181", "leitura", "sbwxdr2d2"),
    SwitchInterfaceStatusFetcher("10.1.80.177", "leitura", "sbwxdr2d2"),
    SwitchInterfaceStatusFetcher("10.1.80.178", "leitura", "sbwxdr2d2"),
    SwitchInterfaceStatusFetcher("10.1.80.173", "leitura", "sbwxdr2d2"),
    SwitchInterfaceStatusFetcher("10.1.80.174", "leitura", "sbwxdr2d2"),
    SwitchInterfaceStatusFetcher("10.1.80.175", "leitura", "sbwxdr2d2"),
]

# Salva tudo em um CSV só
salvar_todos_em_um_csv(switches)
