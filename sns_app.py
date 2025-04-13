import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="whitegrid")
tips=sns.load_dataset("tips")
st.title('mr.prakash senapthi sir seaborn bootcamp tips data visualization app')
st.write("This is a simple app to visualize the tips dataset using seaborn.")
# Function create  and display plot
def display_plot(title, plot_func):
    st.subheader(title)
    fig, ax = plt.subplots(figsize=(8,6))
    plot_func(ax=ax)
    st.pyplot(fig)
    plt.close(fig)
# plot
def scatter_plot(ax):
    sns.scatterplot(data=tips, x="total_bill",y="tip",hue="time",size="size",palette="deep",ax=ax)
    ax.set_title("Scatterplot of Total Bill vs tip")\
        
def line_plot(ax):
    sns.lineplot(data=tips,x="size",y="total_bill",hue='sex',markers='o',ax=ax)
    ax.set_title("lineplot of Total Bill vs Size")
    
def line_plot(ax):
    sns.lineplot(data=tips,x="size",y="total_bill",hue='sex',ci=None,markers='o',ax=ax)
    ax.set_title("lineplot of Total Bill vs Size")

def bar_plot(ax):
     sns.barplot(data=tips,x="day",y="total_bill",hue="sex",palette='muted',ax=ax)
     ax.set_title("Barplot of the total Bill by day")
     
def box_plot(ax):
     sns.boxplot(data=tips,x="day",y="tip",hue="smoker",palette='Set2',ax=ax)
     ax.set_title("Boxplot of Tips by Day and Smoker Status")
     

def violin_plot(ax):
    sns.violinplot(data=tips,x='day',y='total_bill',hue='time',split=True,palette='pastel',ax=ax)
    ax.set_title("violin plot of the Totsl Bill by day and Time") 
    
def count_plot(ax):
    sns.countplot(data=tips,x='day',hue='smoker',palette='dark',ax=ax)
    ax.set_title("count plot of days by smoker status")   
    
def reg_plot(ax):
    sns.regplot(data=tips,x='total_bill',y='tip',scatter_kws={'s':50},line_kws={'color':'red'},ax=ax)
    ax.set_title("Regression plot of Total Bill vs tips")   
    
def hist_plot(ax):
    sns.histplot(data=tips,x='total_bill',bins=20,kde=True,color='blue',ax=ax)
    ax.set_title("Histgram of the Totl Bill with KDE")
    

    
def cat_plot(ax):
    sns.catplot(data=tips,x="day",y="tip",hue="sex",kind="point",palette="bright",ax=ax)
    ax.set_title("catplot(point):Tips by day and gender")
    

    
def FacetGrid(ax):
    g=sns.FacetGrid(tips,col='time',row='smoker',margin_titles=True).map(sns.histplot,'total_bill',bins=20,ax=ax)
    g
    
def strip_plot(ax):
    sns.stripplot(data=tips,x='day',y='tip',hue='sex',jitter=True,palette='Set1',ax=ax)
    ax.set_title("strip plot:Tips by data and gender")
    
def kde_plot(ax):                                                                                       
    sns.kdeplot(data=tips,x='total_bill',hue='sex',fill=True,palette='tab10',ax=ax)
    ax.set_title("kde plot:Total bill density by gender ")
    
display_plot("scatter Plot",scatter_plot)
display_plot("Line Plot",line_plot)
display_plot("Line Plot",line_plot)
display_plot("Bar Plot",bar_plot)
display_plot("Box Plot",box_plot)
display_plot("Violin Plot",violin_plot)
display_plot("Count Plot",count_plot)
display_plot("Regression Plot",reg_plot)
display_plot("Histogram Plot",hist_plot)
display_plot("Cat plot",cat_plot)
display_plot("strip Plot",strip_plot)
display_plot("KDA plot",kde_plot)