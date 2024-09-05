# Accessing an App Viewer's Username

Use dash-enterprise-auth to access the viewer's username in your callbacks. Use this username to display customized data or content depending on who is currently logged in.

## Run the App

> Note: If you initialized your app using an app from the App Catalog, the app's requirements are already installed. Go to step 2 to get started.

1. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```
2. Run the app with:
   ```
   python app.py
   ```

## Deploy the App From Your Workstation

To deploy this app to Dash Enterprise, [initialize an app](https://usprd-dashenterprise.onetakeda.com/docs/dash-enterprise/initialize), and then follow [the steps for deployment](https://usprd-dashenterprise.onetakeda.com/docs/dash-enterprise/deployment).

## Deploy the App From a Workspace

If you're developing your app in a workspace, you can either deploy by selecting the `Deploy` button in the workspace, or by using Git commands in the workspace terminal. See [Deploying Changes](https://usprd-dashenterprise.onetakeda.com/docs/workspaces/deploying-changes) for more details on deploying from a workspace.