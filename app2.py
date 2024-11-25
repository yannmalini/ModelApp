import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# Custom CSS to change background color
st.markdown(
    """
    <style>
    .main {
        background-color: #90CAF9; /* Light blue background */
    }
    .css-18e3th9 {
        font-size: 14px; /* Adjust default font size */
    }
    .css-qbe2hs, .css-1offfwp { /* Smaller font for sidebar elements */
        font-size: 14px;
    }
    .stMarkdown h1, h2, h3, h4, h5, h6 {
        color: #00796B; /* Darker blue-green for headers */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Section: Explanation of the Model
st.title("Methane Emissions in Shrimp Ponds Model")

# Add text to explain the model
st.markdown("""
This Streamlit app models methane (CH₄) emissions in shrimp ponds based on several environmental factors.
""")

st.subheader("What is Methane?")
st.write("Methane (CH₄) is a potent greenhouse gas (GHG) that is colorless, odorless, and highly efficient at trapping heat in the atmospheric. It is produced naturally in wetlands, as a byproduct of the digestion of certain organisms, and through human activities such as agriculture, fossil fuel extraction, and waste management [1].")
st.image("image1.png", caption="Figure 1: Methane (CH4)")

st.subheader("What role do livestock and aquaculture play in methane emissions?")
st.write("Livestock and aquaculture are significant contributors to global emissions of CH₄, CO₂, and N₂O. However, when considering protein production, aquaculture has a lower emission intensity compared to livestock [2]. The relatively low emissions values in aquaculture are primarily due to the lack of enteric methane (CH₄) production and the high fertility and low feed conversion ratios of finfish, crustaceans, and shellfish. This makes aquaculture a more biologically efficient method of producing animal protein compared to terrestrial livestock, especially ruminants [3].")
st.image("image2.png", caption="Figure 2: World production of capture fisheries, aquaculture and pig, chicken and cattle meat from 1961 to 2017.")

st.subheader("Which aquaculture practices emit the most methane?")
st.write("Among aquaculture farming practices, GHG emissions vary based on the farming system, water type, species, production intensity, and water parameters. Crustacean and fish pond-based systems are the leading producers of CH₄. In shrimp ponds, CH₄ is mainly produced in the sediment, where organic waste, uneaten feed, and feces accumulate. Under anaerobic conditions, microorganisms in the sediment decompose this organic matter, generating methane as a byproduct [4].")
st.image("image3.png", caption="Figure 3: Example of shrimp pond.")

st.subheader("Where does methane come from in shrimp (crustacean) ponds?")
st.write("Methane emissions in aquaculture ponds result from the decomposition of organic matter, including uneaten feed, feces, and decaying phytoplankton and zooplankton, which settle in the pond sediment. Under anaerobic conditions, methanogenic archaea and bacteria convert this organic matter into methane (CH₄), alongside intermediate byproducts such as CO₂, NH₃, and H₂S. Key environmental factors like temperature, dissolved oxygen (DO), pH, salinity, and nitrogen influence microbial activity and the rate of methane production. Methane is released to the atmosphere via diffusion or ebullition, highlighting the importance of aquaculture practices and water quality management in mitigating greenhouse gas emissions.")
st.image("image7.png", caption="Figure 4: Explanation on methane production and emission in shrimp ponds [5].")

st.subheader("Description of the three crustacean species in this model")
st.image("image4.png", caption="Figure 5: Whiteleg shrimp.")
st.write("""
**Species**: *Litopenaeus vannamei*  
**Common Name**: Whiteleg Shrimp  
**Origin**: Pacific coast of Latin America  
**Commercial Importance**: 5.5 million tons (2023)  
**Top 3 producers in 2023**: China, India, and Ecuador  
**Production Cycle**: 3–4 months  
**Important Characteristics**: High adaptability, resilience to various salinities, rapid growth, high feed conversion efficiency, and good meat [8].
""")

st.image("image5.png", caption="Figure 6: Black tiger shrimp.")
st.write("""
**Species**: *Penaeus monodon*  
**Common Name**: Black Tiger Shrimp  
**Origin**: Indo-Pacific region  
**Commercial Importance**: 0.9 million tons (2023)  
**Top 3 producers in 2023**: Vietnam, Thailand, and Indonesia  
**Production Cycle**: 4–5 months  
**Important Characteristics**: High disease resistance, robust in high salinity, growth potential, good meat quality, and high market value [7].  
""")

st.image("image6.png", caption="Figure 7: Chinese Mitten Crab.")
st.write("""
**Species**: *Eriocheir sinensis*  
**Common Name**: Chinese Mitten Crab  
**Origin**: East Asia (China, Korea)  
**Commercial Importance**: 0.5 million tons (2023)  
**Top 3 producers in 2023**: China, South Korea, and Japan  
**Production Cycle**: 6–8 months  
**Important Characteristics**: High market value, adaptability to low salinity, resilience in fluctuating conditions, strong burrowing behavior, quality meat [8].  
""")

# Environmental Conditions Table
st.subheader("Environmental Conditions")
st.write("""Table 1: Ideal water parameters for the crustacean species""")
data = {
    "Parameter": [
        "Temperature (°C)", "Salinity (ppt)", "pH", "Dissolved Oxygen (DO, mg/L)", "Total Nitrogen (TN, µg/L)",
        "Total Organic Carbon (TOC, mg/L)", "Alkalinity (mg/L CaCO₃)", "Ammonia (NH₃, µg/L)",
        "Nitrite (NO₂⁻, µg/L)", "Hardness (mg/L CaCO₃)"
    ],
    "*Litopenaeus vannamei* (Whiteleg Shrimp)": ["26–32", "5–20", "7.5–8.5", ">5", "<1,000", "<20", "80–200", "<100", "<500", "100–300"],
    "*Penaeus monodon* (Black Tiger Shrimp)": ["28–32", "10–25", "7.5–8.5", ">4", "<1,000", "<20", "100–200", "<100", "<500", "100–250"],
    "*Eriocheir sinensis* (Chinese Mitten Crab)": ["18–28", "0–15 (ideally 5–10)", "7.5–8.5", ">5", "<500", "<15", "50–150", "<100", "<500", "50–200"]
}
df = pd.DataFrame(data)
st.dataframe(df)

st.subheader("Impact on CH₄ flux")
st.write("""
- **Temperature**: Higher temperatures increase microbial metabolic rates in pond sediments, accelerating the organic matter decomposition and increasing methane production.  
- **Total Organic Carbon (TOC)**: Higher TOC levels provide more fuel for methanogenic microorganisms, increasing methane production.  
- **Salinity**: Elevated salinity generally suppresses methane production because saline conditions can inhibit methanogenic microorganisms.  
- **Nitrogen**: Nitrogen compounds can affect methane flux by impacting microbial communities in the sediment.  
- **Dissolved Oxygen (DO)**: Higher DO levels suppress CH₄ flux by reducing anaerobic zones in pond sediments.  
- **pH**: Methanogens prefer a neutral to slightly alkaline pH. Extreme pH levels can inhibit these microorganisms.  
""")

st.subheader("Goals of this app and project")
st.write("This app aims to model methane emissions in shrimp (or crab) pond systems and examine how various environmental parameters affect methane flux.")

st.subheader("Now let’s predict the methane emissions from shrimp (or crabs) ponds:")
st.write("""
**First step**: Choose a species among *Litopenaeus vannamei*, *Penaeus monodon*, or *Eriocheir sinensis*.  
**Second step**: Select the water parameters of your pond. You can check the ideal parameters for each species in the table above.  
**Third step**: Run the model.  

The model calculates methane emissions using a mechanistic function based on these inputs, allowing you to adjust values and observe changes in predicted methane flux.
""")

# Define methane emission model function
def methane_emission_model(alpha, beta_1, beta_2, beta_3, beta_4, beta_5, beta_6, temp, TOC, salinity, nitrogen, DO, pH):
    methane_flux = (
        alpha 
        * np.exp(np.clip(beta_1 * temp, -50, 50))          # Temperature effect
        * (np.clip(TOC, 5, None) ** beta_2)             # TOC effect
        * (np.clip(salinity, 1e-10, None) ** beta_3)        # Salinity effect
        * np.exp(np.clip(-beta_4 * nitrogen, -50, 50))      # Nitrogen effect
        / np.exp(np.clip(beta_5 * DO, -50, 50))             # DO effect (now beta_5 = -0.01)
        * (np.clip(pH, 1e-10, None) ** beta_6)              # pH effect
    )
    return methane_flux

# Set default model parameters
alpha = 1.0
beta_1 = 0.1
beta_2 = 1.0
beta_3 = -0.5
beta_4 = 0.01
beta_5 = -0.01  # Updated to -0.01 as specified
beta_6 = 0.05

# Streamlit interface
st.title("Methane Emissions in Shrimp Ponds Model")

# Sidebar for model parameter inputs
st.sidebar.header("Model Parameters")
temp = st.sidebar.slider("Temperature (°C)", 1, 40, 27)
TOC = st.sidebar.slider("Total Organic Carbon (mg/L)", 5, 30, 15)
salinity = st.sidebar.slider("Salinity (ppt)", 1, 40, 10)
nitrogen = st.sidebar.slider("Nitrogen (µg/L)", 50, 2000, 100)
DO = st.sidebar.slider("Dissolved Oxygen (mg/L)", 2, 15, 5)
pH = st.sidebar.slider("pH", 6.0, 9.0, 7.5, step=0.1)

# Dropdown to choose the x-axis parameter for the plot
x_axis_param = st.sidebar.selectbox("Select X-axis Parameter", ["Temperature", "TOC", "Salinity", "Nitrogen", "DO", "pH"])

# Set up the x-axis data based on the selected parameter
if x_axis_param == "Temperature":
    x_values = np.linspace(10, 40, 100)
    methane_flux_values = [methane_emission_model(alpha, beta_1, beta_2, beta_3, beta_4, beta_5, beta_6, x, TOC, salinity, nitrogen, DO, pH) for x in x_values]
elif x_axis_param == "TOC":
    x_values = np.linspace(5, 30, 100)
    methane_flux_values = [methane_emission_model(alpha, beta_1, beta_2, beta_3, beta_4, beta_5, beta_6, temp, x, salinity, nitrogen, DO, pH) for x in x_values]
elif x_axis_param == "Salinity":
    x_values = np.linspace(1, 40, 100)
    methane_flux_values = [methane_emission_model(alpha, beta_1, beta_2, beta_3, beta_4, beta_5, beta_6, temp, TOC, x, nitrogen, DO, pH) for x in x_values]
elif x_axis_param == "Nitrogen":
    x_values = np.linspace(50, 200, 100)
    methane_flux_values = [methane_emission_model(alpha, beta_1, beta_2, beta_3, beta_4, beta_5, beta_6, temp, TOC, salinity, x, DO, pH) for x in x_values]
elif x_axis_param == "DO":
    x_values = np.linspace(2, 15, 100)
    methane_flux_values = [methane_emission_model(alpha, beta_1, beta_2, beta_3, beta_4, beta_5, beta_6, temp, TOC, salinity, nitrogen, x, pH) for x in x_values]
elif x_axis_param == "pH":
    x_values = np.linspace(6.0, 9.0, 100)
    methane_flux_values = [methane_emission_model(alpha, beta_1, beta_2, beta_3, beta_4, beta_5, beta_6, temp, TOC, salinity, nitrogen, DO, x) for x in x_values]

# Create an interactive plot with Plotly
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=x_values,
    y=methane_flux_values,
    mode='lines+markers',
    name="Methane Flux",
    marker=dict(size=5),
    hovertemplate="CH₄ Flux: %{y:.2f} mg CH₄/m²/day<br>" + f"{x_axis_param}: " + "%{x:.2f}<extra></extra>"
))

# Customize the layout
fig.update_layout(
    title=f"Effect of {x_axis_param} on Methane Flux",
    xaxis_title=x_axis_param,
    yaxis_title="Methane Flux (mg CH₄/m²/day)",
    hovermode="x unified"
)

# Display the plot in Streamlit
st.plotly_chart(fig)

# Title and Description
st.title("Methane Emissions Model Overview")

# Section: Model Equation and Variables
st.subheader("Model Equation")
st.write("The model estimates methane emissions (CH₄ flux) in shrimp ponds based on a combination of environmental variables as shown in the equation below:")
st.latex(r"CH_4 \, \text{flux} = \alpha \times e^{(\beta_1 \cdot \text{Temp})} \times (\text{TOC})^{\beta_2} \times (\text{Salinity})^{\beta_3} \times e^{(-\beta_4 \cdot \text{Nitrogen})} \div e^{(\beta_5 \cdot \text{DO})} \times (\text{pH})^{\beta_6}")

st.write("Where:")
st.markdown("""
- **CH₄ flux**: Methane emissions in mg CH₄/m²/day.
- **Temp**: Temperature (°C).
- **TOC**: Total Organic Carbon (mg/L), representing organic matter available for decomposition.
- **Salinity**: Salinity level (ppt), with higher salinity often suppressing methane production.
- **Nitrogen**: Total nitrogen concentration (µg/L), which can indirectly affect microbial activity.
- **DO**: Dissolved Oxygen (mg/L), where higher levels typically reduce methane production.
- **pH**: pH level, with methanogens preferring neutral to slightly alkaline conditions.
- **α, β₁, β₂, β₃, β₄, β₅, β₆**: Model parameters that are calibrated based on experimental data.

Each variable reflects environmental conditions impacting microbial metabolism and organic matter breakdown, influencing methane production levels in shrimp ponds.

""")

# Section: Dataset Origin and Details
st.title("This section provides insights into the dataset used in the methane emission model. ")
st.subheader("Dataset Origin and Composition")
st.write("The dataset used in this model analysis was compiled from a variety of sources to provide comprehensive methane emission data across aquaculture studies. Here are key details:")

st.markdown("""
- **Number of Articles**: 71
- **Geographic Coverage**: Asia and South America
- **Species Covered**: 
    - *Litopenaeus vannamei* (Whiteleg Shrimp): 38
    - *Penaeus monodon* (Black Tiger Shrimp): 2
    - *Eriocheir sinensis* (Chinese Mitten Crab): 24
    - Other species: 7

This dataset reflects data from various regions and species, allowing for a robust model to analyze methane emissions across different aquaculture conditions.
""")

st.write("Explore the distribution of studies across countries and analyze the annual trsnds in study counts.")

# Load dataset from the Excel file directly
data_file = 'DataModels.xlsx'
sheet_name = 'ArticleInfo' 
try:
    data = pd.read_excel(data_file)
    sheet_name = 'ArticleInfo' 

    # Ensure data is a DataFrame and check for correct column names
    if not isinstance(data, pd.DataFrame):
        st.error("Data was not loaded as a DataFrame. Check the file path and format.")
    else:
        # Check if the necessary columns exist
        required_columns = ['Country', 'Year', 'DOI']
        if not all(column in data.columns for column in required_columns):
            st.error("One or more required columns are missing in the dataset.")
        else:
            # Count the number of studies per country
            country_counts = data['Country'].value_counts().reset_index()
            country_counts.columns = ['Country', 'Count']

            # Count the number of studies per year
            year_counts = data['Year'].value_counts().sort_index().reset_index()
            year_counts.columns = ['Year', 'Count']

            # Plot a world map with a heatmap indicating the number of studies per country
            st.subheader("Global Distribution of Studies by Country")
            fig_country = px.choropleth(
                country_counts,
                locations="Country",
                locationmode="country names",
                color="Count",
                hover_name="Country",
                color_continuous_scale="Viridis",
            )
            fig_country.update_geos(showcoastlines=True, coastlinecolor="Black", showland=True, landcolor="lightgrey")
            fig_country.update_layout(coloraxis_colorbar=dict(title="Number of Studies"))
            st.plotly_chart(fig_country)

            # Plot a bar plot for the number of studies by year
            st.subheader("Number of Studies by Year")
            fig_year = px.bar(
                year_counts,
                x='Year',
                y='Count',
                labels={'Count': 'Number of Studies', 'Year': 'Year'}
            )
            st.plotly_chart(fig_year)

            # References Section
            st.subheader("References of the Dataset")
            unique_dois = data['DOI'].drop_duplicates().dropna()  # Remove duplicates and NaN values
            with st.expander("Click here to view the list of DOI references"):
                for doi in unique_dois:
                    st.write(doi)

except FileNotFoundError:
    st.error("The file 'DataModels.xlsx' was not found. Please check the file path and make sure it's available.")


# References with smaller font size
st.markdown("""
<div class="reference-text">


1. Runkov, R. A., & Ilyasov, D. V. (2024). Spatial variability of methane emissions from soils of wet forests: A brief review. *Environmental Dynamics and Global Climate Change*, 14(3), 167–180. https://doi.org/10.18822/edgcc375293  

2. Dong, H., Zhao, Y., Lu, X., Cai, Y., Yang, J., He, M., ... & Zhang, X. (2023). Quantifying methane emissions from aquaculture ponds in China. *Environmental Science & Technology*. https://doi.org/10.1021/acs.est.2c05218  

3.  MacLeod, M. J., Hasan, M. R., Robb, D. H. F., & Mamun-Ur-Rashid, M. (2020). Quantifying greenhouse gas emissions from global aquaculture. Scientific Reports, 10(1), 11679. https://doi.org/10.1038/s41598-020-68231-8

4. Yang, P., Lai, D. Y. F., Yang, H., Tong, C., Lebel, L., Huang, J., & Xu, J. (2019). Methane dynamics of aquaculture shrimp ponds in two subtropical estuaries, southeast China: Dissolved concentration, net sediment release, and water oxidation. *Journal of Geophysical Research: Biogeosciences*, 124(6), 1430–1445. https://doi.org/10.1029/2018JG004794  

5. Tan, J., Lichtfouse, E., Luo, M., Liu, Y., Tan, F., Zhang, C., Chen, X., Huang, J., & Xiao, L. (2023). Aquaculture drastically increases methane production by favoring acetoclastic rather than hydrogenotrophic methanogenesis in shrimp pond sediments. Aquaculture, 563, 738999. https://doi.org/10.1016/j.aquaculture.2022.738999
 
6. Dugassa, H., & Gaetan, D. G. (2018). Biology of white leg shrimp, *Penaeus vannamei*: Review. *World Journal of Fish and Marine Sciences*, 10(2), 5–17. https://doi.org/10.5829/idosi.wjfms.2018.05.17  

7. Alfaro-Montoya, J., Monge-Ortiz, A. M., Martínez-Fernández, D., & Herrera-Quesada, E. (2015). First record of the nonindigenous *Penaeus monodon* Fabricius, 1798 (*Penaeidae*) in the Caribbean Sea of Costa Rica, Central America, with observations on selected aspects of its reproductive biology. *BioInvasions Records*, 4(3), 217–222. https://doi.org/10.3391/bir.2015.4.3.11  

8. Veilleux, É., & de Lafontaine, Y. (2007). Biological synopsis of the Chinese mitten crab (*Eriocheir sinensis*). *Canadian Manuscript Report of Fisheries and Aquatic Sciences*, 2812, vi + 45.
</div>
""", unsafe_allow_html=True)

# Footer Section with About and Contact Information
st.markdown("""
    <hr style="border:1px solid #00796B;">
    <div style="font-size: 10px; text-align: center;">
        <p><strong>About the Project</strong></p>
        <p>This project, "Methane Emissions in Shrimp Ponds," was developed by Yann Malini Ferreira, a PhD student in the Department of Animal Biosciences at the University of Guelph. This model was created as part of the final project for the course <strong>ANSC*6030 - Modeling Metabolic Processes</strong>, under the guidance of <strong>Professor Dr. John Cant</strong>.</p>
        <p>Contact & Additional Resources</p>
        <p>For further information or collaboration opportunities, please reach out via email: <a href="mailto:yannmalini@yahoo.com">yannmalini@yahoo.com</a></p>
    </div>
""", unsafe_allow_html=True)

# Add logos side by side using columns
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    st.image("logo1.png", caption="University of Guelph", use_container_width=True)

with col2:
    st.image("logo2.png", caption="Department of Animal Biosciences", use_container_width=True)

with col3:
    st.image("logo3.png", caption="Centre for Nutrition Modelling", use_container_width=True)
