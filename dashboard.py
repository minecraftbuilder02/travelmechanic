import streamlit as st
import plotly.express as px
import pandas as pd
import os
import warnings
from PIL import Image
import base64
from io import BytesIO

# Suppress warnings
warnings.filterwarnings('ignore')

# Function to convert image to Base64 string
def get_base64_image(image_path):
    try:
        img = Image.open(image_path)
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        return base64.b64encode(buffered.getvalue()).decode()
    except Exception as e:
        st.error(f"Error loading image: {e}")
        return None

# Set the page icon to the custom image (using base64)
icon_path = "travel_mechanic.jpg"  # Ensure this file is in the correct directory
base64_icon = get_base64_image(icon_path)
if base64_icon:
    st.set_page_config(page_title="Travel Mechanic", page_icon=Image.open(icon_path), layout="wide")
else:
    st.set_page_config(page_title="Travel Mechanic", layout="wide")

# Login Credentials
USER_CREDENTIALS = {"admin": "123", "user1": "123"}

# Function for Home Page
def home_page():
    # Menu Bar with Login and Services Link
    st.markdown("""<style>
        .menu-bar {
            background-color: #2c3e50;
            padding: 10px;
            text-align: center;
        }
        .menu-bar a {
            color: white;
            font-size: 18px;
            margin: 0 20px;
            text-decoration: none;
        }
        .menu-bar a:hover {
            color: #ecf0f1;
        }
    </style>""", unsafe_allow_html=True)

    st.markdown('<div class="menu-bar"> <a href="#" onClick="window.location.reload()">Home</a> <a href="#about">About</a> <a href="#services">Services</a></div>', unsafe_allow_html=True)
    
    # Login button positioned at top right
    st.markdown("""
    <style>
        .login-btn {
            position: absolute;
            top: 60px;  /* Adjust this value to make it below the menu bar */
            right: 30px;
        }
    </style>
    """, unsafe_allow_html=True)

    if st.button("Login", key="login_btn", help="Login", use_container_width=False):
        st.session_state["page"] = "login"

    # Home Page Content with updated background and logo
    st.markdown(
        f"""
        <h1 style="text-align: center; color: white;">Welcome to Travel Mechanic</h1>
        <div style="background-image: url('data:image/jpg;base64,{get_base64_image("bgb.jpg")}'); height: 100vh; background-size: cover; text-align: center; color: white; font-size: 30px; display: flex; justify-content: center; align-items: center;">
            <p></p>
        </div>
        """, unsafe_allow_html=True)

    # About Section (for scrolling)
    st.markdown(
        """
        <div id="about" style="padding: 40px; text-align: center; max-width: 800px; margin: 0 auto;">
    <h2>About Travel Mechanic</h2>
    <p>
        Automotive Technician. We do home services to repair your car.<br>
        We travel CALABARZON and METRO MANILA areas.<br>
        Free check-up and consultation for walk-in clients.<br>
        Our services are quality and affordable.
    </p>
</div>
        """, unsafe_allow_html=True)

    # "Our Services" Section with 6 images (4, 5, 6 added)
    st.markdown("<div id='services'><h2 style='text-align: center;'>Our Services</h2></div>", unsafe_allow_html=True)
    
    image_paths = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg", "6.jpg"]  # Example image paths
    image_html = ""

    # Create a row with 3 columns for the first 3 images
    col1, col2, col3 = st.columns(3)

    for i, col in enumerate([col1, col2, col3]):
        if i < len(image_paths):  # Ensure the image index is within range
            img_base64 = get_base64_image(image_paths[i])
            if img_base64:
                col.image(f"data:image/jpeg;base64,{img_base64}", use_column_width=True)
            else:
                col.warning(f"Image {image_paths[i]} not found or cannot be loaded.")
    
    # Create another row with 3 columns for the next 3 images
    col1, col2, col3 = st.columns(3)

    for i, col in enumerate([col1, col2, col3]):
        if i + 3 < len(image_paths):  # Ensure the image index is within range
            img_base64 = get_base64_image(image_paths[i + 3])
            if img_base64:
                col.image(f"data:image/jpeg;base64,{img_base64}", use_column_width=True)
            else:
                col.warning(f"Image {image_paths[i + 3]} not found or cannot be loaded.")

    # Footer
    st.markdown(
    """
    <footer style="background-color: #2c3e50; color: white; padding: 20px;">
        <!-- First Row: Location, Contact, Email, Facebook -->
        <div style="display: flex; justify-content: space-between; text-align: left; padding: 10px;">
            <!-- Location -->
            <div style="flex: 1; padding-right: 10px;">
                <p>Dasmariñas, Philippines</p>
            </div>
            <!-- Contact Number -->
            <div style="flex: 1; padding-right: 10px;">
                <p>0970 034 9288</p>
            </div>
            <!-- Email -->
            <div style="flex: 1; padding-right: 10px;">
                <p>
                    <a href="mailto:travelmechanic14@gmail.com" style="color: white; text-decoration: none;">
                        travelmechanic14@gmail.com
                    </a>
                </p>
            </div>
            <!-- Facebook -->
            <div style="flex: 1; text-align: right;">
                <p>
                    <a href="https://www.facebook.com/katrame2021" style="color: white; text-decoration: none;" target="_blank">
                        Facebook
                    </a>
                </p>
            </div>
        </div>
        <!-- Second Row: All Rights Reserved -->
        <div style="text-align: center; padding-top: 10px; border-top: 1px solid white; margin-top: 10px;">
            <p>© 2024 Travel Mechanic. All Rights Reserved.</p>
        </div>
    </footer>
    """, unsafe_allow_html=True)


# Function for login
def login():
    st.title("Login")

    # Custom CSS to create a two-column layout
    st.markdown("""<style>
        .login-container {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 80vh;
            max-width: 1000px; /* Set a maximum width for the container */
            margin: 0 auto; /* Center the container horizontally */
        }
        .left-column, .right-column {
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            padding: 20px;
            gap: 10px;
        }
        .left-column {
            width: 40%; /* Adjust the width as needed */
        }
        .right-column {
            width: 60%; /* Adjust the width as needed */
        }
        .login-form {
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        h1 {
            text-align: center;
            font-size: 2.5rem;
        }
    </style>""", unsafe_allow_html=True)

    # Create a container to center the columns and make sure both columns share the center
    with st.container():
        col1, col2 = st.columns([1, 1])  # Both columns share equal space

        # Left Column: "Back to Home" Button, Description & Logo
        with col1:
            # Back to Home Button (First line of col1)
            if st.button("Back to Home"):
                st.session_state["page"] = "home"  # Reset page to home
                
            st.markdown("<h2>Welcome to Travel Mechanic</h2>", unsafe_allow_html=True)    

            # Logo
            st.markdown(f'<img src="data:image/png;base64,{get_base64_image("travel_mechanic.jpg")}" width="200">', unsafe_allow_html=True)

        # Right Column: Login Form
        with col2:
            # Login Form - Ensure this part is centered
            with st.container():
                username = st.text_input("Username")
                password = st.text_input("Password", type="password")
                if st.button("Login"):
                    if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
                        st.session_state["logged_in"] = True
                        st.success("Logged in successfully!")
                        st.session_state["page"] = "main"
                    else:
                        st.error("Invalid username or password")



# Main App function
def main_app():
    st.markdown(
        f"""
        <div style="display: flex; align-items: center;">
            <img src="data:image/png;base64,{base64_icon}" width="50" style="margin-right: 10px;">
            <h1 style="margin: 0; display: inline-block;">Data of Travel Mechanic</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<style>div.block-container{padding-top:2rem;}<style>', unsafe_allow_html=True)

    # File uploader
    fl = st.file_uploader(":file_folder: Upload a file", type=(["csv", "txt", "xlsx", "xls"]))

    # Step 1: Handle file upload or use local fallback
    if fl is not None:
        try:
            # Handle file format and read into DataFrame
            filename = fl.name
            if filename.endswith(".csv"):
                df = pd.read_csv(fl)
            else:
                df = pd.read_excel(fl, "Sheet1")
            st.success("File uploaded successfully!")
        except Exception as e:
            st.error(f"Error loading the file: {e}")
            st.stop()
    else:
        # Use default local file
        os.chdir(os.path.dirname(__file__))
        df = pd.read_excel("Travelmechanic.xlsx", "Sheet1")  
        st.info("Using default file from local storage.")

    

    # Standardize column names (strip spaces and check if the 'Repair' column exists)
    df.columns = df.columns.str.strip()  # Strip spaces in column names

    if "Repair" not in df.columns:
        st.error("The 'Repair' column is missing or named incorrectly!")
        st.stop()

    if "Cost" in df.columns:
        df["Cost"] = pd.to_numeric(df["Cost"], errors='coerce')  # Convert to numeric
    else:
        st.error("The 'Cost' column is missing or named incorrectly!")
        st.stop()

    if "Date" in df.columns:
        # Ensure 'Date' column is parsed as datetime
        df["Date"] = pd.to_datetime(df["Date"], errors='coerce')
        if df["Date"].isna().any():
            st.write(f"")
    else:
        st.error("The 'Date' column is missing or named incorrectly!")
        st.stop()



    # Sidebar with filters and logout button
    st.sidebar.header("Choose your filter:")

    # Vehicle filter
    vehicles = st.sidebar.multiselect("Pick your Vehicle", df["Vehicle"].dropna().unique())

    # Repair filter
    repairs = st.sidebar.multiselect("Pick Repair Type", df["Repair"].dropna().unique())

    # Date filter (formatted to remove time)
    df["Formatted Date"] = df["Date"].dt.strftime('%Y-%m-%d')  # Format date for display
    dates = st.sidebar.multiselect("Pick Date", df["Formatted Date"].unique())  # Use formatted dates

    # Month filter (formatted)
    df["Month"] = df["Date"].dt.strftime("%B %Y")  # Example: "January 2024"
    months = st.sidebar.multiselect("Pick Month", df["Month"].unique())

    # Apply filters dynamically
    filtered_df = df.copy()

    # Vehicle filter
    if vehicles:
        filtered_df = filtered_df[filtered_df["Vehicle"].isin(vehicles)]

    # Repair type filter
    if repairs:
        filtered_df = filtered_df[filtered_df["Repair"].isin(repairs)]

    # Date filter
    if dates:
        filtered_df = filtered_df[filtered_df["Formatted Date"].isin(dates)]

    # Month filter
    if months:
        filtered_df = filtered_df[filtered_df["Month"].isin(months)]

    # Reset to original dataframe if no filters are applied
    if not (vehicles or repairs or dates or months):
        filtered_df = df.copy()

    # Add space before the logout button to position it lower
    st.sidebar.markdown("<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>", unsafe_allow_html=True)

    # Logout Button at the bottom of the sidebar
    if st.sidebar.button("Logout"):
        st.session_state["logged_in"] = False
        st.session_state["page"] = "home"
        st.experimental_rerun()



    # Apply filters dynamically
    filtered_df = df.copy()

    # Vehicle filter
    if vehicles:
        filtered_df = filtered_df[filtered_df["Vehicle"].isin(vehicles)]

    # Repair type filter
    if repairs:
        filtered_df = filtered_df[filtered_df["Repair"].isin(repairs)]

    # Date filter (if exact dates are chosen)
    if dates:
        filtered_df = filtered_df[filtered_df["Date"].dt.strftime('%Y-%m-%d').isin(dates)]

    # Month filter (for formatted month strings like "January 2024")
    if months:
        filtered_df = filtered_df[filtered_df["Month"].isin(months)]

    # Reset to original dataframe if no filters are applied
    if not (vehicles or repairs or dates or months):
        filtered_df = df.copy()


    # Group by Date for the bar chart
    category_df = filtered_df.groupby(by=["Date"], as_index=False)["Cost"].sum()

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Date-wise Cost")
        if not category_df.empty:
            fig = px.bar(
                category_df,
                x="Date",
                y="Cost",
                text=[f'{x:,.2f}' for x in category_df["Cost"]],
                template="seaborn"
            )
            # Adjust layout for readability
            fig.update_layout(
                xaxis=dict(tickangle=45),
                margin=dict(l=10, r=10, t=50, b=80),
                height=300
            )
            fig.update_traces(
                textposition="outside",
                textfont_size=10
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.write("No data to display.")

    with col2:
        st.subheader("Vehicle-wise Cost")
        if not filtered_df.empty:
            fig = px.pie(
                filtered_df,
                values="Cost",
                names="Vehicle",
                hole=0.5
            )
            # Adjust layout
            fig.update_traces(
                textinfo="percent+label",
                textfont_size=12,
                pull=[0.1] * filtered_df["Vehicle"].nunique()
            )
            fig.update_layout(
                height=400,
                margin=dict(l=20, r=20, t=50, b=50)
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.write("No data to display.")

    # Count or sum costs by repair type
    repair_costs = filtered_df.groupby("Repair")["Cost"].sum().reset_index().sort_values(by="Cost", ascending=False)

    fig = px.bar(
        repair_costs,
        x="Repair",
        y="Cost",
        title="Cost by Repair Type",
        text="Cost",
        template="seaborn"
    )
    fig.update_layout(xaxis=dict(tickangle=45), height=400)
    st.plotly_chart(fig, use_container_width=True)

    # Box plot for repair cost distribution
    fig = px.box(
        filtered_df,
        x="Repair",
        y="Cost",
        title="Repair Cost Distribution",
        points="all"  # Shows all points including outliers
    )
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)

    # Heatmap for cost distribution by vehicle and date
    heatmap_data = filtered_df.pivot_table(values="Cost", index="Vehicle", columns="Date", aggfunc="sum", fill_value=0)
    fig = px.imshow(
        heatmap_data,
        title="Cost Heatmap by Vehicle and Date",
        color_continuous_scale="Viridis"
    )
    st.plotly_chart(fig, use_container_width=True)

    # Dynamic filtering using a slider for cost range
    min_cost, max_cost = st.slider("Select Cost Range", int(filtered_df["Cost"].min()), int(filtered_df["Cost"].max()), (1000, 10000))
    cost_filtered_df = filtered_df[(filtered_df["Cost"] >= min_cost) & (filtered_df["Cost"] <= max_cost)]

    st.write("Filtered Data:")
    st.write(cost_filtered_df)

    # Group by month for cost trends
    filtered_df["Month"] = filtered_df["Date"].dt.to_period('M')  # Convert to monthly period
    monthly_costs = (
        filtered_df.groupby("Month")["Cost"]
        .sum()
        .reset_index()
        .sort_values("Month")
    )

    # Interactive Summary Cards
    total_cost = filtered_df["Cost"].sum()
    total_repairs = len(filtered_df)
    most_expensive_vehicle = filtered_df.groupby("Vehicle")["Cost"].sum().idxmax()

    st.metric(label="Total Cost (PHP)", value=f"{total_cost:,.2f}")
    st.metric(label="Total Repairs", value=total_repairs)
    st.metric(label="Most Expensive Vehicle", value=most_expensive_vehicle)

# Check session state for login and page navigation
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if "page" not in st.session_state:
    st.session_state["page"] = "home"

# Page Flow Logic
if st.session_state["page"] == "home":
    home_page()
elif st.session_state["page"] == "login":
    login()
elif st.session_state["page"] == "main" and st.session_state["logged_in"]:
    main_app()
