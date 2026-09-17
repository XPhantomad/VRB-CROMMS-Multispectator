
import subprocess

import ipywidgets as widgets
from IPython.display import display


class SutTeleopLauncher:
    def __init__(self, repo_root: str, ros_setup: str, teleop_script: str):
        self.repo_root = repo_root
        self.ros_setup = ros_setup
        self.teleop_script = teleop_script
        self.processes = {}  # sut_number -> subprocess.Popen
        self._build_widgets()

    # ---------------- launching ----------------

    def _launch(self, sut_number: int):
        script = f"""
            cd {self.repo_root}
            source {self.ros_setup}
            python3 {self.teleop_script} {sut_number}
            """
        proc = subprocess.Popen(["gnome-terminal", "--", "bash", "-c", script])
        self.processes[sut_number] = proc
        self._log(f'SUT {sut_number}: Terminal geöffnet (PID {proc.pid}).')

    def close_all(self):
        for sut_number, proc in list(self.processes.items()):
            if proc.poll() is None:  # noch am Laufen
                proc.terminate()
                self._log(f'SUT {sut_number}: Terminal beendet.')
        self.processes.clear()

    # ---------------- widget side ----------------

    def _log(self, msg: str):
        with self.output:
            print(msg)

    def _on_launch_click(self, _):
        sut_number = self.number_field.value
        self._launch(sut_number)

    def _build_widgets(self):
        self.number_field = widgets.BoundedIntText(
            value=1, min=1, max=5, step=1,
            description='SUT-Nr.:',
            layout=widgets.Layout(width='150px'),
        )
        launch_btn = widgets.Button(
            description='Teleop starten',
            button_style='success',
            icon='play',
        )
        close_btn = widgets.Button(
            description='Alle schließen',
            button_style='danger',
            icon='stop',
        )
        launch_btn.on_click(self._on_launch_click)
        close_btn.on_click(lambda _: self.close_all())

        self.output = widgets.Output(
            layout=widgets.Layout(border='1px solid #ccc', height='120px', overflow='auto')
        )

        self.widget_box = widgets.VBox([
            widgets.HBox([self.number_field, launch_btn, close_btn]),
            self.output,
        ])

    def show(self):
        display(self.widget_box)