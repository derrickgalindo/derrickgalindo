"""Inline CSS and data into the playbook page template -> report/roblox-hit-playbook.html"""
import os
R = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "report")
t = open(os.path.join(R, "template.html")).read()
t = t.replace("__CSS__", open(os.path.join(R, "_base.css")).read()).replace("__DATA__", open(os.path.join(R, "roblox_data.json")).read())
open(os.path.join(R, "roblox-hit-playbook.html"), "w").write(t)
print("ok", len(t))
