import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

def plot_workflow_durations(csv_filepath='workflow_data_for_plot.csv', output_image_filepath='workflow_stacked_bar_chart.png'):
    """
    Genarate a stacked bar chart of workflow execution times
    Args:
        csv_filepath (str): input csv file
        output_image_filepath (str): output image file path

    Returns:
    """
    try:
        data = pd.read_csv(csv_filepath, names=['date', 'execution_id', 'duration_seconds'])
    except FileNotFoundError:
        print(f"Error: '{csv_filepath}' not found.")
        return
    except Exception as e:
        print(f"Error: reading csv file '{csv_filepath}':{e}")
        return

    data['date'] = pd.to_datetime(data['date'])
    print("CSV file read: ---")
    print(data.head())
    print("\ndata info:")
    print(data.info())

    if data['duration_seconds'].dtype == 'object':
        data['duration_seconds'] = data['duration_seconds'].astype(str).str.replace('s', '', regex=False)
        print("duration seconds removed 's':---")
        print(data.head())
        print("\ndata info:")
        print(data.info())

    data['duration_seconds'] = pd.to_numeric(data['duration_seconds'], errors='coerce')
    if data['duration_seconds'].isnull().any():
        print("Warning: 'duration_seconds' contained unparseable values. filled with NaN")
    
    print("duration seconds: numeric ---")
    print(data.head())
    print("\ndata info:")
    print(data.info())
    data['duration_seconds'] = data['duration_seconds'].round(2)
    print("duration seconds: round ---")
    print(data.head())
    print("\ndata info:")
    print(data.info())

    # Aggregate duration by date and execution ID: x(date), y(execution), values(sec)
    pivot_df = data.pivot_table(index='date', columns='execution_id', values='duration_seconds', aggfunc='sum')

    # padding for missing valuse
    pivot_df = pivot_df.fillna(0)

    # make plot area
    plt.figure(figsize=(14, 8)) 
    ax = plt.gca()
    pivot_df.plot(kind='bar', stacked=True, ax=ax, width=0.8)
    
    # adjustment
    max_total_duration = pivot_df.sum(axis=1).max()
    print(f"max total duration: {max_total_duration:.2f} s")
    if pd.isna(max_total_duration) or max_total_duration <= 0.0:
        ax.set_ylim(0, 0.5)
        major_interval = 0.1
        minor_interval = 0.05
        print("Warning: max total duration is null or invarid. set dafault value for y-axiss")
    else:
        ax.set_ylim(0, max_total_duration * 1.2)

        if max_total_duration <= 1.0:
            major_interval = 0.1
            minor_interval = 0.05
        elif max_total_duration <= 5.0:
            major_interval = 0.5
            minor_interval = 0.1
        elif max_total_duration <= 10.0:
            major_interval = 1.0
            minor_interval = 0.5
        elif max_total_duration <= 50.0:
            major_interval = 5.0
            minor_interval = 1.0
        elif max_total_duration <= 100.0:
            major_interval = 10.0
            minor_interval = 2.0 
        else: # longer 
            major_interval = round(max_total_duration / 5 / 5) * 5
            if major_interval < 1: major_interval = 1.0
            minor_interval = major_interval / 5

    ax.yaxis.set_major_locator(MultipleLocator(major_interval))
    ax.yaxis.set_minor_locator(MultipleLocator(minor_interval))
    print(f"max Y: {ax.get_ylim()[1]:.2f} s, scale: major={major_interval}s, minor={minor_interval}s")
      
    # title label
    plt.title('Daily Workflow Execution Duration by Execution ID')
    plt.xlabel('Start Date')
    plt.ylabel('Total Execution Duration (seconds)')
    plt.xticks(rotation=45, ha='right')
    plt.legend(title='Execution ID', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig(output_image_filepath)
    print(f"graph file '{output_image_filepath}' generated.")

if __name__ == '__main__':
    plot_workflow_durations(csv_filepath='wfex.csv', output_image_filepath='wfchart.png')
