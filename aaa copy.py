import subprocess
import os

class SuaClasse:
   

    def restore(self):
        # Define database connection details
        host = "192.168.1.2"
        port = 1001  # Change this line to use an integer
        user = "LUCAS"
        password = "THMPV.2022"
        database = "pdv"
        backup_file = "backup19.11.2023.sql"

        # Substitua o caminho completo para o mysql no seu sistema
        mysql_path = r"C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe"

        # Build the mysql command for restore
        restore_command = [mysql_path, "-h", host, "-u", user, "-p" + password, database]

        # Open a subprocess with stdin as a pipe
        process = subprocess.Popen(restore_command, stdin=subprocess.PIPE)

        # Read the contents of the backup file
        with open(backup_file, 'rb') as f:
            backup_data = f.read()

        # Pass the backup data to the subprocess for restore
        process.communicate(input=backup_data)

        print("Restore completed successfully.")


# Exemplo de uso
minha_classe = SuaClasse()
# Executa o backup

# Executa o restore
minha_classe.restore()
