# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from uuid import UUID

from mercury_banking._runtime import (
    AsyncDownload,
    AsyncResource,
    Download,
    Operation,
    Param,
    Resource,
    Scheme,
    checked,
)

_get_statement_pdf: Operation[None] = Operation(
    id="getStatementPdf",
    method="GET",
    path="/statements/{statementId}/pdf",
    resource="statements",
    name="download_pdf",
    params=(Param("statementId", "statement_id", "path"),),
    response=None,
    binary_response=True,
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)

OPERATIONS = (_get_statement_pdf,)


class StatementsApi(Resource):
    @checked
    def download_pdf(
        self,
        statement_id: UUID,
    ) -> Download:
        """Download an account statement as a PDF. Close the download, or read it in a `with` block."""
        return self._download(
            _get_statement_pdf,
            statement_id=statement_id,
        )


class AsyncStatementsApi(AsyncResource):
    @checked
    async def download_pdf(
        self,
        statement_id: UUID,
    ) -> AsyncDownload:
        """Download an account statement as a PDF. Close the download, or read it in an `async with` block."""
        return await self._download(
            _get_statement_pdf,
            statement_id=statement_id,
        )
