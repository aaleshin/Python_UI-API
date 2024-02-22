# Настройкa
# 1) генерируем ключ
ssh-keygen : интер - потом фразу пароль
# 2) To start the agent, run the following:
ls ~/.ssh   
# 3) To start the agent, run the following:
eval `ssh-agent` 
# 4) Enter ssh-add followed by the path to the private key file:
macOS:  $ ssh-add -K ~/.ssh/id_rsa      
Linux:  $ ssh-add ~/.ssh/id_rsa 
# 5) copy publick key
macOS:   pbcopy < ~/.ssh/id_rsa.pub
  Linux:   cat ~/.ssh/id_rsa.pub
# 6) add key to bitbucket
Personal settings from your avatar -> SSH keys > add key
# 7) check:
ssh -T git@bitbucket.org
# 8) install libraries
pip install -r requirements.txt
# 9) Install Allure
Linux:
sudo apt-add-repository ppa:qameta/allure
sudo apt-get update 
sudo apt-get install allure

Mac OS X:
brew install allure

# create allure report:
# allure generate -c ./reports
# allure serve ./reports