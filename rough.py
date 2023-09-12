import pandas as pd
import matplotlib.pyplot as plt
import textwrap  # Import the textwrap module

# Sample data in a Pandas Series
data = pd.Series([0.15, 0.30, 0.45, 0.20], index=['Category A', 'Category B', 'Category C', 'Category D'])

# Find the maximum and minimum values
max_value = data.max()
min_value = data.min()

# Create a figure with a specific size
fig = plt.figure(figsize=(10, 6))  # Set the figure size to 10 inches (width) by 6 inches (height)

# Create a grid for the layout
grid = plt.GridSpec(100, 100, hspace=0.2, wspace=0.2)

# Create the horizontal bar graph (70% to the right)
ax = fig.add_subplot(grid[:, 30:])  # Adjust the number of columns to control the width

# Customize grid lines: Change the linestyle to 'dashed'
ax.grid(True, linestyle='--', color='gray', linewidth=0.5)  # Set the linestyle, color, and linewidth

# Create the text area (30% top left)
text_area = fig.add_subplot(grid[:30, :30])
text_area.set_xticks([])  # Remove x-axis ticks
text_area.set_yticks([])  # Remove y-axis ticks
text_area.grid(False)  # Disable grid lines for the text area

# Create the legend area (30% bottom left)
legend_area = fig.add_subplot(grid[70:, :30])
legend_area.set_xticks([])  # Remove x-axis ticks
legend_area.set_yticks([])  # Remove y-axis ticks
legend_area.grid(False)  # Disable grid lines for the legend area

# Create a horizontal bar graph with custom colors and reduced bar width
data.plot(kind='barh', color=['blue' for _ in data.index], width=0.5, ax=ax)  # Adjust the width as needed

# Labeling and customization for the main graph
ax.set_xlabel('Values (%)')  # Set the x-axis label with the percentage symbol
ax.set_ylabel('Categories')
ax.set_title('Horizontal Bar Graph with Custom Bar Colors and Reduced Bar Width')

# Set the x-axis (horizontal) limits based on the maximum value
ax.set_xlim(0, max_value * 1.5)  # Adjust the multiplier (1.5) as needed

# Remove the top and right spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Remove ticks from the right and top sides of the graph
ax.tick_params(axis='both', which='both', right=False, top=False)

# Annotate each bar with percentage values and color based on min/max values
for i, v in enumerate(data):
    percentage = f'{v * 100:.2f}%'  # Convert to percentage format with 2 decimal places and add %
    color = 'green' if v == max_value else 'red' if v == min_value else 'blue'
    ax.text(v + 0.005, i, percentage, va='center', fontsize=10, color=color, fontweight='bold')  # Adjust the position (v + 0.005) as needed

# Manually adjust the linestyle for the right side of the y-axis to remove dashed lines at labelright
# ax.yaxis.set_tick_params(which='both', right=False, linestyle='-')

# Add vertical lines at the xlim limits
ax.axvline(0, color='gray', linestyle='--', linewidth=1)
#ax.axvline(max_value * 1.5, color='gray', linestyle='--', linewidth=1)

# Wrap the long text and set the multialignment to 'center'
text_to_add = "This is a very long text that needs to be placed below the graph, and it can span multiple lines as needed."
wrapped_text = textwrap.fill(text_to_add, width=30)  # Adjust the width as needed
text_area.text(0.5, -0.2, wrapped_text, fontsize=12, fontweight='bold', va='center', ha='center', transform=text_area.transAxes, multialignment='center')

# Create a custom legend with square-shaped colored markers and no labels
legend_colors = ['blue', 'red', 'green', 'orange']

# Create legend handles with colored square markers and no labels
legend_handles = [plt.Line2D([0], [0], marker='s', markersize=10, color=color) for color in legend_colors]

# Add the legend with square markers (no labels) to the legend area
legend_area.legend(handles=legend_handles, loc='upper left', fontsize=10)

# Save the graph to a .fig file
#plt.savefig('horizontal_bar_graph_with_legend_square_markers_no_labels.fig', format='fig')

# Show the graph (optional)
plt.show()
