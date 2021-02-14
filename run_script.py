# Contributions-Importer-For-Github/run_script.py
import git
from git_contributions_importer import *

# Your private repo or Bitbucket repo
repo = git.Repo("https://sherifelsayed@bitbucket.org/ureedteam/ureed_flutter.git")
# Your mock repo
mock_repo = git.Repo("https://github.com/sherifhasan/mock-repo.git")
importer = Importer([repo], mock_repo)
# I use both my personal email and work email here,
# Since the private repo uses work email, and Github profiles uses
# my work email
importer.set_author(['sherif.hasan1994@gmail.com', 'sherif.elsayed@ureed.com'])
importer.import_repository()