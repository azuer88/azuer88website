def git_pull():
	"updates the repository."
	run("cd ~/git/$(repo)/; git pull $(parent) $(branch)")

def git_reset():
	"Resets the repository to specified version."
	run("cd ~/git/$(repo)/; git reset --hard $(hash)")


def production():
	pass
