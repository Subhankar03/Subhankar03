import json
import streamlit as st

st.set_page_config(page_title="Subhankar Dutta", page_icon='💼', layout='wide')
st.html('style.css')
with open('projects.json') as f:
	projects = json.load(f)

# Profile pic and title (custom HTML)
st.html('''
<div style="display: flex; align-items: center; gap: clamp(15px, 5vw, 30px); margin-bottom: 24px;">
    <img src="app/static/profile-pic.png" alt="Profile Picture" class="profile-picture">
    <h1>Subhankar Dutta</h1>
</div>
''')

# Create tabs for navigation
about_me, my_projects, contact_me = st.tabs(["About Me", "My Projects", "Contact Me"])

# About me section
with about_me:
	# Add a resume download option
	st.html('''
	<a class="resume-btn" href="https://drive.google.com/uc?export=download&id=1LnaJYm1U8372kEyH5zNXOis7wsejEu0Q" download="Resume–Data Analyst–Subhankar Dutta.pdf">
		<svg xmlns="http://www.w3.org/2000/svg" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
			<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/>
			<polyline points="7 10 12 15 17 10"/>
			<line x1="12" y1="15" x2="12" y2="3"/>
		</svg>
		Download resume
	</a>
	''')
	with open('README.md', encoding='utf-8') as f:
		st.write(f.read(), unsafe_allow_html=True)

# My projects section
with my_projects:
	# Create a 2-column grid
	cols = st.columns(ncols:=3)

	# Iterate through projects and display them in the grid
	for i, (project_name, project_info) in enumerate(projects.items()):
		with cols[i % ncols]:
			# Display the image with a clickable link
			st.html(f'''
				<a href="{project_info['url']}" target="_blank">
					<img src="{project_info['preview']}" class="project-preview">
				</a>
			''')
			st.page_link(project_info['url'], label=project_name)
			st.write('')

# Contact me section
with contact_me:
	st.html('''
		<img src='app/static/icons/phone-call.png' width='16'> &nbsp; Call me at:&nbsp;
		<a href="tel:+918240545068">+91 8240545068</a>
	''')
	st.html('''
		<img src='app/static/icons/email.png' width='16'> &nbsp; E-mail me at:&nbsp;
		<a href="mailto:sankardutta7358@gmail.com">sankardutta7358@gmail.com</a>
	''')
	st.html('''
		<img src='app/static/icons/linkedin.png' width='16'> &nbsp; Connect me on LinkedIn:&nbsp;
		<a href="https://linkedin.com/in/SubhankarDutta03">https://linkedin.com/in/SubhankarDutta03</a>
	''')
	st.html('''
		<img src='app/static/icons/github.png' width='16'> &nbsp; See my GitHub profile:&nbsp;
		<a href="https://github.com/Subhankar03">https://github.com/Subhankar03</a>
	''')
