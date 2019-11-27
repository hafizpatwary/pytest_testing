pipeline{
	agent any

	stages{
		stage('--Install pytest as Jenkins--'){
			steps{
				sh "pip3 install pytest"
				sh "python3 --version"
				sh "/usr/lib/python3/dist-packages/pytest"
			}
		}
		stage('--Printing current working directorty--'){
			steps{
				sh "pwd "
			}
		}
		stage('--Test--'){
			steps{
				sh "pytest"
			}
		}
		stage('--list--'){
			steps{
				sh "echo 'previous stage worked'"
			}
		}
	}
}