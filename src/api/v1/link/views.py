from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse, Response

from ...pydantic.models import Pagination

from src.domain.link.models import LinkUpdateDTO, LinkCreateDTO
from src.domain.link.repository import AbstractLinkRepository, LinkNotFoundError

from .models import LinkSchema, ListLinkSchema, LinkCreateSchema, LinkUpdateSchema
from .dependecies import get_link_repo


router = APIRouter(prefix="/link")


@router.get("/{link_id}", response_model=LinkSchema)
async def get_link(link_id: int, repo: AbstractLinkRepository = Depends(get_link_repo)) -> JSONResponse:
    try:
        link = repo.get(link_id)
    except LinkNotFoundError as exc:
        print(exc)
        return JSONResponse({}, status_code=status.HTTP_404_NOT_FOUND)

    link_schema = LinkSchema(
        id=link.id,
        original_url=link.original_url,
        short_url=link.short_url,
    )

    return JSONResponse(link_schema.model_dump(mode="json"), status_code=status.HTTP_200_OK)


@router.get("", response_model=ListLinkSchema)
async def list_links(pagination: Pagination = Depends(), repo: AbstractLinkRepository = Depends(get_link_repo)) -> JSONResponse:
    links = repo.list(limit=pagination.limit, offset=pagination.offset)
    content = [
        ListLinkSchema(
            id=link.id,
            original_url=link.original_url,
            short_url=link.short_url,
        ).model_dump(mode="json")
        for link in links
    ]

    return JSONResponse(content=content, status_code=status.HTTP_200_OK)


@router.post("", response_model=LinkSchema)
async def create_link(payload: LinkCreateSchema, repo: AbstractLinkRepository = Depends(get_link_repo)) -> JSONResponse:
    dto = LinkCreateDTO(
        original_url=payload.original_url,
        short_url=payload.short_url,
    )

    link = repo.create(dto)

    link_schema = LinkSchema(
        id=link.id,
        original_url=link.original_url,
        short_url=link.short_url,
    )

    return JSONResponse(link_schema.model_dump(mode="json"), status_code=status.HTTP_201_CREATED)


@router.patch("/{link_id}", response_model=LinkSchema)
async def update_link(link_id: int, payload: LinkUpdateSchema, repo: AbstractLinkRepository = Depends(get_link_repo)) -> JSONResponse:
    dto = LinkUpdateDTO(
        original_url=payload.original_url,
        short_url=payload.short_url,
    )

    try:
        link = repo.update(link_id, dto)
    except LinkNotFoundError as exc:
        print(exc)
        return JSONResponse({}, status_code=status.HTTP_404_NOT_FOUND)

    link_schema = LinkSchema(
        id=link_id,
        original_url=link.original_url,
        short_url=link.short_url,
    )

    return JSONResponse(link_schema.model_dump(mode="json"), status_code=status.HTTP_200_OK)


@router.delete("/{link_id}", response_model=LinkSchema)
async def delete(link_id: int, repo: AbstractLinkRepository = Depends(get_link_repo)):
    try:
        repo.delete(link_id)
    except LinkNotFoundError as exc:
        print(exc)
        return JSONResponse({}, status_code=status.HTTP_404_NOT_FOUND)
    return Response(status_code=status.HTTP_204_NO_CONTENT)