# FAWATERI

## Entity Relationship Diagram (ERD).

![ERD](assets/ERD.svg)

## Routing Table

### Users
<table border="1" width="100%">
    <thead>
        <tr>
            <th width="20%">HTTP Method</th>
            <th width="40%">Path</th>
            <th width="40%">Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>GET</td>
            <td>/users/signup/</td>
            <td>Create new user account.</td>
        </tr>
        <tr>
            <td>POST</td>
            <td>/users/login/</td>
            <td>Log in to an existing user account.</td>
        </tr>
        <tr>
            <td>DELET</td>
            <td>users/token/refresh/</td>
            <td>Verify user credentials and permissions.</td>
        </tr>
    </tbody>
</table>

### Bills
<table border="1" width="100%">
    <thead>
        <tr>
            <th width="20%">HTTP Method</th>
            <th width="40%">Path</th>
            <th width="40%">Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>GET</td>
            <td>/bills</td>
            <td>List All Bills</td>
        </tr>
        <tr>
            <td>GET</td>
            <td>/bills/{id}</td>
            <td>Show details of Bill</td>
        </tr>
        <tr>
            <td>POST</td>
            <td>/bills</td>
            <td>create new bill</td>
        </tr>
        <tr>
            <td>PUT</td>
            <td>/bills/{id}</td>
            <td>Update bill details</td>
        </tr>
        <tr>
            <td>DELETE</td>
            <td>/bills/{id}</td>
            <td>Delete bill</td>
        </tr>
    </tbody>
</table>

### Catagories
<table border="1" width="100%">
    <thead>
        <tr>
            <th width="20%">HTTP Method</th>
            <th width="40%">Path</th>
            <th width="40%">Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>GET</td>
            <td>/catagories</td>
            <td>List All catagories</td>
        </tr>
        <tr>
            <td>GET</td>
            <td>/catagories/{id}</td>
            <td>Show details of catagory</td>
        </tr>
        <tr>
            <td>POST</td>
            <td>/catagories</td>
            <td>create new catagory</td>
        </tr>
        <tr>
            <td>PUT</td>
            <td>/catagories/{id}</td>
            <td>Update catagory details</td>
        </tr>
        <tr>
            <td>DELETE</td>
            <td>/catagories/{id}</td>
            <td>Delete catagory</td>
        </tr>
    </tbody>
</table>

### Reminders
<table border="1" width="100%">
    <thead>
        <tr>
            <th width="20%">HTTP Method</th>
            <th width="40%">Path</th>
            <th width="40%">Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>GET</td>
            <td>/bills/{bill_id}/reminders</td>
            <td>List All reminders of bill.</td>
        </tr>
        <tr>
            <td>POST</td>
            <td>/bills/{bill_id}/reminders</td>
            <td>create new reminder for bill.</td>
        </tr>
        <tr>
            <td>DELET</td>
            <td>reminders/{reminder_id}</td>
            <td>Delete reminder.</td>
        </tr>
    </tbody>
</table>

### Images
<table border="1" width="100%">
    <thead>
        <tr>
            <th width="20%">HTTP Method</th>
            <th width="40%">Path</th>
            <th width="40%">Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>GET</td>
            <td>/bills/{bill_id}/image</td>
            <td>Get bill image.</td>
        </tr>
        <tr>
            <td>POST</td>
            <td>/bills/{bill_id}/image</td>
            <td>Add new Image to bill.</td>
        </tr>
        <tr>
            <td>DELETE</td>
            <td>/image/{image_id}</td>
            <td>Delete Image.</td>
        </tr>
    </tbody>
</table>

### Bills & Catagories (M:M Relation):
<table border="1" width="100%">
    <thead>
        <tr>
            <th width="20%">HTTP Method</th>
            <th width="40%">Path</th>
            <th width="40%">Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>GET</td>
            <td>/bills/{bill_id}/catagories</td>
            <td>List categories on a bill</td>
        </tr>
        <tr>
            <td>POST</td>
            <td>/bills/{bill_id}/catagories/{catagory_id}</td>
            <td>Attach categories</td>
        </tr>
        <tr>
            <td>DELETE</td>
            <td>/bills/{bill_id}/catagories/{catagory_id}</td>
            <td>Delete catagory from bill</td>
        </tr>
    </tbody>
</table>
