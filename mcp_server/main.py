# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-29T01:54:39+00:00



import argparse
import json
import os
from typing import *
from typing import Optional

from autogen.mcp.mcp_proxy import MCPProxy
from autogen.mcp.mcp_proxy.security import BaseSecurity, UnsuportedSecurityStub
from fastapi import Path, Query

from models import (
    Alt,
    FieldXgafv,
    GoogleApiHttpBody,
    GoogleCloudDiscoveryengineV1betaDocument,
    GoogleCloudDiscoveryengineV1betaImportDocumentsRequest,
    GoogleCloudDiscoveryengineV1betaImportUserEventsRequest,
    GoogleCloudDiscoveryengineV1betaListDocumentsResponse,
    GoogleCloudDiscoveryengineV1betaRecommendRequest,
    GoogleCloudDiscoveryengineV1betaRecommendResponse,
    GoogleCloudDiscoveryengineV1betaUserEvent,
    GoogleLongrunningListOperationsResponse,
    GoogleLongrunningOperation,
    GoogleProtobufEmpty,
)

app = MCPProxy(
    contact={'name': 'Google', 'url': 'https://google.com', 'x-twitter': 'youtube'},
    description='Discovery Engine API.',
    license={
        'name': 'Creative Commons Attribution 3.0',
        'url': 'http://creativecommons.org/licenses/by/3.0/',
    },
    termsOfService='https://developers.google.com/terms/',
    title='Discovery Engine API',
    version='v1beta',
    servers=[{'url': 'https://discoveryengine.googleapis.com/'}],
)


@app.delete(
    '/v1beta/{name}',
    description=""" Deletes a Document. """,
    tags=['project_operation_handling'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def delete_project_document(
    name: str,
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1beta/{name}',
    description=""" Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service. """,
    tags=['project_operation_handling', 'service_recommendation'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def discoveryengine_projects_operations_get(
    name: str,
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.patch(
    '/v1beta/{name}',
    description=""" Updates a Document. """,
    tags=['document_operations', 'project_operation_handling'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def patch_project_document(
    name: str,
    allow_missing: Optional[bool] = Query(None, alias='allowMissing'),
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
    body: GoogleCloudDiscoveryengineV1betaDocument = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1beta/{name}/operations',
    description=""" Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`. """,
    tags=['project_operation_handling', 'user_event_collection'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def discoveryengine_projects_operations_list(
    name: str,
    filter: Optional[str] = None,
    page_size: Optional[int] = Query(None, alias='pageSize'),
    page_token: Optional[str] = Query(None, alias='pageToken'),
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1beta/{parent}/documents',
    description=""" Gets a list of Documents. """,
    tags=['project_operation_handling'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def list_document_branches_for_project(
    parent: str,
    page_size: Optional[int] = Query(None, alias='pageSize'),
    page_token: Optional[str] = Query(None, alias='pageToken'),
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1beta/{parent}/documents',
    description=""" Creates a Document. """,
    tags=['document_operations', 'project_operation_handling'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def create_document_in_discovery_engine(
    parent: str,
    document_id: Optional[str] = Query(None, alias='documentId'),
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
    body: GoogleCloudDiscoveryengineV1betaDocument = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1beta/{parent}/documents:import',
    description=""" Bulk import of multiple Documents. Request processing may be synchronous. Non-existing items will be created. Note: It is possible for a subset of the Documents to be successfully updated. """,
    tags=['document_operations', 'user_event_collection', 'project_operation_handling'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def import_documents_for_discovery_engine(
    parent: str,
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
    body: GoogleCloudDiscoveryengineV1betaImportDocumentsRequest = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1beta/{parent}/userEvents:collect',
    description=""" Writes a single user event from the browser. This uses a GET request to due to browser restriction of POST-ing to a 3rd party domain. This method is used only by the Discovery Engine API JavaScript pixel and Google Tag Manager. Users should not call this method directly. """,
    tags=['user_event_collection', 'project_operation_handling'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def collect_user_events_from_data_store(
    parent: str,
    ets: Optional[str] = None,
    uri: Optional[str] = None,
    user_event: Optional[str] = Query(None, alias='userEvent'),
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1beta/{parent}/userEvents:import',
    description=""" Bulk import of User events. Request processing might be synchronous. Events that already exist are skipped. Use this method for backfilling historical user events. Operation.response is of type ImportResponse. Note that it is possible for a subset of the items to be successfully inserted. Operation.metadata is of type ImportMetadata. """,
    tags=['user_event_collection', 'project_operation_handling'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def import_user_events_for_project(
    parent: str,
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
    body: GoogleCloudDiscoveryengineV1betaImportUserEventsRequest = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1beta/{parent}/userEvents:write',
    description=""" Writes a single user event. """,
    tags=['user_event_collection'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def discoveryengine_projects_locations_data_stores_user_events_write(
    parent: str,
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
    body: GoogleCloudDiscoveryengineV1betaUserEvent = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1beta/{servingConfig}:recommend',
    description=""" Makes a recommendation, which requires a contextual user event. """,
    tags=['service_recommendation'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def recommend_service_configurations(
    serving_config: str = Path(..., alias='servingConfig'),
    field__xgafv: Optional[FieldXgafv] = Query(None, alias='$.xgafv'),
    access_token: Optional[str] = None,
    alt: Optional[Alt] = None,
    callback: Optional[str] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    upload_protocol: Optional[str] = None,
    upload_type: Optional[str] = Query(None, alias='uploadType'),
    body: GoogleCloudDiscoveryengineV1betaRecommendRequest = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MCP Server")
    parser.add_argument(
        "transport",
        choices=["stdio", "sse", "streamable-http"],
        help="Transport mode (stdio, sse or streamable-http)",
    )
    args = parser.parse_args()

    if "CONFIG_PATH" in os.environ:
        config_path = os.environ["CONFIG_PATH"]
        app.load_configuration(config_path)

    if "CONFIG" in os.environ:
        config = os.environ["CONFIG"]
        app.load_configuration_from_string(config)

    if "SECURITY" in os.environ:
        security_params = BaseSecurity.parse_security_parameters_from_env(
            os.environ,
        )

        app.set_security_params(security_params)

    mcp_settings = json.loads(os.environ.get("MCP_SETTINGS", "{}"))

    app.get_mcp(**mcp_settings).run(transport=args.transport)
