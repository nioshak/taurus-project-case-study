import streamlit as st
import graphviz

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Taurus Space | Project Case Study",
    page_icon="🚀",
    layout="wide"
)

# --- SIDEBAR: CONTEXT & GOVERNANCE ---
with st.sidebar:
    st.image("https://img.icons8.com/color/96/000000/satellite-sending-signal.png", width=50) # Placeholder Icon
    st.title("Taurus Space")
    st.caption("Secure Geospatial Analytics Platform")
    
    st.divider()
    
    # Simulating a Governance Toggle
    user_role = st.radio(
        "View Perspective:",
        ["Executive Summary", "Technical Architecture", "Delivery Metrics"]
    )
    
    st.info(
        """
        **Context:**
        This portal demonstrates the TPM strategy used to deliver a dual-use (Commercial & Defense) logistics platform.
        
        *Data has been sanitized for public viewing.*
        """
    )

# --- MAIN CONTENT ---

st.title("Project: Dual-Use Autonomous Logistics")
st.markdown("### *Bridging the Gap Between Commercial Velocity and Defense Compliance*")

# --- SECTION 1: EXECUTIVE SUMMARY ---
if user_role == "Executive Summary":
    st.subheader("The Challenge")
    col1, col2 = st.columns(2)
    with col1:
        st.warning(
            "**Conflict of Interest:**\n\n"
            "• **Commercial Customers** demanded rapid feature iteration (CI/CD) and public cloud APIs.\n"
            "• **Defense Customers** required air-gapped deployments (IL-5) and rigid static binaries."
        )
    with col2:
        st.success(
            "**The Solution:**\n\n"
            "• Implemented a 'Core-Common' modular architecture.\n"
            "• Built a unified 'Software Factory' pipeline that forks only at the final build stage.\n"
            "• **Result:** Single codebase serving both sectors."
        )

    st.divider()
    
    st.subheader("Impact at a Glance")
    m1, m2, m3 = st.columns(3)
    m1.metric(label="Deployment Time", value="3 Days", delta="-40%")
    m2.metric(label="Code Reusability", value="85%", help="Core logic shared between comms & defense")
    m3.metric(label="Compliance", value="FedRAMP Ready", help="Verified via automated security gates")

# --- SECTION 2: ARCHITECTURE (THE TECHNICAL FLEX) ---
elif user_role == "Technical Architecture":
    st.subheader("System Design: The 'Hybrid' Core")
    st.write("How we architected a single platform to serve two opposing deployment environments.")
    
    # Graphviz Diagram - Proves you understand system design
    arch_diag = graphviz.Digraph()
    arch_diag.attr(rankdir='LR') # Left to Right
    
    # Nodes
    arch_diag.node('A', 'Dev Team', shape='box', style='filled', fillcolor='#e1f5fe')
    arch_diag.node('B', 'Unified Repo\n(GitLab)', shape='cylinder')
    arch_diag.node('C', 'CI/CD Pipeline\n(Security Scans)', shape='box')
    
    arch_diag.node('D', 'Build Fork', shape='diamond', style='filled', fillcolor='#fff9c4')
    
    arch_diag.node('E', 'Commercial Artifact\n(Docker/K8s)', shape='note', style='filled', fillcolor='#dcedc8')
    arch_diag.node('F', 'Defense Artifact\n(Hardened Binary)', shape='note', style='filled', fillcolor='#ffccbc')
    
    # Edges
    arch_diag.edge('A', 'B', label='Push Code')
    arch_diag.edge('B', 'C', label='Trigger')
    arch_diag.edge('C', 'D', label='Passes Gates')
    arch_diag.edge('D', 'E', label='Route A')
    arch_diag.edge('D', 'F', label='Route B (Air Gap)')
    
    st.graphviz_chart(arch_diag)
    
    with st.expander("See Technical Details"):
        st.markdown("""
        * **Container Strategy:** Commercial uses standard lightweight containers; Defense uses hardened Iron Bank base images.
        * **RBAC:** Identity management abstracts the auth provider (Auth0 for Commercial vs. CAC/Piv for Defense).
        """)

# --- SECTION 3: METRICS ---
elif user_role == "Delivery Metrics":
    st.subheader("Operational Efficiency")
    
    # Simple dataframe to show you handle data
    import pandas as pd
    
    data = {
        "Metric": ["Release Frequency", "Security Incidents", "Onboarding Time", "Infra Costs"],
        "Before Strategy": ["Monthly", "4/Quarter", "6 Weeks", "$5k/mo"],
        "After Strategy": ["Bi-Weekly", "0/Quarter", "1 Week", "$1k/mo"],
        "Improvement": ["2x Faster", "100% Reduction", "83% Faster", "80% Savings"]
    }
    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)
    
    st.bar_chart({"Commercial Users": 85, "Defense Nodes": 14})

# --- FOOTER ---
st.divider()
st.caption("Author: N.Kayhani • Built using Streamlit • Deployed via GitHub Actions • Sanitized for Public Viewing")



