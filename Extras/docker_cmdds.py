from docker_cmd.common import command_executes
from abc import ABC, abstractmethod


class AbsDockerLib(ABC):
    @abstractmethod
    def stop_container(self, c_name):
        pass

    @abstractmethod
    def start_container(self, c_name):
        pass

    @abstractmethod
    def exec_commands_in_container(self, c_name, cmds):
        pass

    @abstractmethod
    def delete_container(self, c_name):
        pass

    @abstractmethod
    def pull_container(self, c_name):
        pass

    def run_container(self, c_name):
        pass


class DockerLib(AbsDockerLib):

    def stop_container(self, c_name):
        """

        :return:
        """
        cmd = "docker stop " + c_name
        out, err = command_executes(cmd)

        return out, err

    def start_container(self, c_name):
        """

        :return:
        """
        cmd = "docker start " + c_name
        out, err = command_executes(cmd)

        return out, err

    def exec_commands_in_container(self, c_name, cmds):
        """

        :return:
        """
        cmd = "docker exec " + c_name + cmds
        out, err = command_executes(cmd)

        return out, err

    def delete_container(self, c_name):
        """

        :return:
        """
        cmd = "docker rm -f " + c_name
        out, err = command_executes(cmd)

        return out, err

    def pull_container(self, c_name):
        """

        :return:
        """
        cmd = "docker pull " + c_name
        out, err = command_executes(cmd)

        return out, err

    def run_container(self, c_name):
        """

        :return:
        """
        cmd = "docker run -dit " + c_name
        out, err = command_executes(cmd)

        return out, err


execute_docker = DockerLib()
# print(execute_docker.pull_container("ubuntu"))
print(execute_docker.run_container("vibrant_mestorf "))
# print(execute_docker.start_container("vibrant_mestorf "))
print(execute_docker.exec_commands_in_container("vibrant_mestorf ", " ls -a "))
# print(execute_docker.stop_container("vibrant_mestorf "))
# print(execute_docker.delete_container("epic_wu "))
