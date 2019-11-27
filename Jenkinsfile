pipeline{
	agent any

	stages{
		stage('--Install pytest as Jenkins--'){
			steps{
				sh "pip3 install pytest"
				sh "python3 --version"
				sh "python3 /usr/lib/python3/dist-packages/pytest.py"
			}
		}
		stage('--Printing current working directorty--'){
			steps{
				sh "pwd "
			}
		}
		stage('--list--'){
			steps{
				sh "echo 'previous stage worked'"
			}
		}
	}
}