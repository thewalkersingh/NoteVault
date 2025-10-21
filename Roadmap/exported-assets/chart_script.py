import plotly.graph_objects as go
import plotly.express as px

# Data for the Backend Java Developer roadmap
data = {
    "phases": [
        {"phase": "Foundation", "months": "1-2", "key_topics": "Java Basics, OOP, Collections", "level": "Beginner"},
        {"phase": "Database Foundations", "months": "2", "key_topics": "SQL, JDBC, Database Design", "level": "Beginner"},
        {"phase": "Spring Core", "months": "3-4", "key_topics": "Spring Boot, DI, MVC", "level": "Intermediate"},
        {"phase": "Data Access", "months": "4", "key_topics": "Spring Data JPA, Hibernate", "level": "Intermediate"},
        {"phase": "Security", "months": "5", "key_topics": "Spring Security, OAuth2, JWT", "level": "Intermediate"},
        {"phase": "Testing", "months": "6", "key_topics": "JUnit, Mockito, Integration Tests", "level": "Intermediate"},
        {"phase": "Microservices", "months": "7-8", "key_topics": "Spring Cloud, Docker, APIs", "level": "Advanced"},
        {"phase": "System Design", "months": "8-9", "key_topics": "Scalability, Patterns, Architecture", "level": "Advanced"},
        {"phase": "DevOps", "months": "10", "key_topics": "CI/CD, Monitoring, Performance", "level": "Advanced"},
        {"phase": "Specialization", "months": "10-12", "key_topics": "Advanced Java, NoSQL, Events", "level": "Expert"}
    ]
}

# Parse months and prepare data
phases_data = []
for i, phase_info in enumerate(data["phases"]):
    months_str = phase_info["months"]
    if "-" in months_str:
        start_month, end_month = map(int, months_str.split("-"))
    else:
        start_month = end_month = int(months_str)
    
    # For single month phases, add 0.8 duration for visibility
    duration = end_month - start_month + 1
    if duration == 1:
        actual_end = start_month + 0.8
    else:
        actual_end = end_month
    
    phases_data.append({
        "Phase": phase_info["phase"],
        "Start": start_month,
        "End": actual_end,
        "Level": phase_info["level"],
        "Topics": phase_info["key_topics"],
        "Row": i
    })

# Color mapping for levels
level_colors = {
    "Beginner": "#1FB8CD",
    "Intermediate": "#DB4545", 
    "Advanced": "#2E8B57",
    "Expert": "#5D878F"
}

# Create figure
fig = go.Figure()

# Add rectangles for each phase
for phase in phases_data:
    fig.add_trace(go.Scatter(
        x=[phase["Start"], phase["End"], phase["End"], phase["Start"], phase["Start"]],
        y=[phase["Row"]-0.4, phase["Row"]-0.4, phase["Row"]+0.4, phase["Row"]+0.4, phase["Row"]-0.4],
        fill="toself",
        fillcolor=level_colors[phase["Level"]],
        line=dict(color=level_colors[phase["Level"]], width=2),
        mode="lines",
        name=phase["Level"],
        hovertemplate=f"<b>{phase['Phase']}</b><br>" +
                     f"Months: {phase['Start']}" + (f"-{int(phase['End'])}" if phase['End'] != phase['Start'] else "") + "<br>" +
                     f"Level: {phase['Level']}<br>" +
                     f"Skills: {phase['Topics']}<extra></extra>",
        showlegend=False
    ))

# Add phase labels
for phase in phases_data:
    # Shorten phase names to fit better
    phase_name = phase["Phase"]
    if len(phase_name) > 12:
        if "Database" in phase_name:
            phase_name = "DB Foundations"
        elif "Microservices" in phase_name:
            phase_name = "Microservice"
        elif "Specialization" in phase_name:
            phase_name = "Specializing"
        else:
            phase_name = phase_name[:12]
    
    # Use white text for darker colors, black for lighter
    text_color = "white" if phase["Level"] in ["Advanced", "Expert", "Intermediate"] else "black"
    
    fig.add_trace(go.Scatter(
        x=[(phase["Start"] + phase["End"]) / 2],
        y=[phase["Row"]],
        mode='text',
        text=[phase_name],
        textposition="middle center",
        textfont=dict(color=text_color, size=12, family="Arial"),
        showlegend=False,
        hoverinfo="skip"
    ))

# Add legend traces manually to control order
level_order = ["Beginner", "Intermediate", "Advanced", "Expert"]
for level in level_order:
    fig.add_trace(go.Scatter(
        x=[None], y=[None],
        mode='markers',
        marker=dict(color=level_colors[level], size=12),
        name=level,
        showlegend=True
    ))

# Update layout
fig.update_layout(
    title="Backend Java Dev Learning Path",
    xaxis_title="Month",
    yaxis_title="Learning Phase",
    xaxis=dict(
        tickmode='linear',
        tick0=1,
        dtick=1,
        range=[0.5, 12.5],
        gridcolor='rgba(200,200,200,0.3)',
        gridwidth=1,
        showgrid=True
    ),
    yaxis=dict(
        tickmode='array',
        tickvals=list(range(len(phases_data))),
        ticktext=[phase["phase"] for phase in data["phases"]],
        range=[-0.8, len(phases_data) - 0.2],
        gridcolor='rgba(200,200,200,0.3)',
        gridwidth=1,
        showgrid=True
    ),
    legend=dict(
        orientation='h',
        yanchor='bottom',
        y=1.05,
        xanchor='center',
        x=0.5
    ),
    showlegend=True,
    plot_bgcolor='white'
)

fig.update_traces(cliponaxis=False)

# Save the chart
fig.write_image("java_backend_roadmap.png")