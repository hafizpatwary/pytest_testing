pipeline{
	agent any

	stages{
		stage('Get source code'){
			steps{
				sh "pip3 install pytest"
			}
		}
		stage('--Test--'){
			steps{
				sh "pytest"
			}
		}
		stage('--list--'){
			steps{
				sh "echo previous stage worked"
			}
		}
	}
}