ARG PYTHON_VERSION=3.14.0

FROM python:$PYTHON_VERSION-bookworm AS base_build

ARG RUNUSER=app \
    USERID=500 \
    GROUPID=500 \
    UV_VERSION=0.9.7 \
    PIP_VERSION=25.3 \
    APP_DIR=/data/app

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_DEFAULT_TIMEOUT=100 \
    UV_SYSTEM_PYTHON=true \
    UV_PYTHON="python$PYTHON_VERSION" \
    UV_PYTHON_DOWNLOADS=never \
    UV_COMPILE_BYTECODE=1 \
    UV_PROJECT_ENVIRONMENT=/data/.venv \
    UV_LINK_MODE=copy \
    UV_CACHE_DIR=/data/.cache/uv

ENV PATH="$UV_PROJECT_ENVIRONMENT/bin:$PATH"

SHELL ["/bin/bash", "-eo", "pipefail", "-c"]

RUN echo "Europe/Moscow" > /etc/timezone && cp -v "/usr/share/zoneinfo/Europe/Moscow" /etc/localtime \
    && apt-get update && apt-get upgrade -y \
    && apt-get install --no-install-recommends -y bash brotli build-essential gcc curl gettext libpq-dev libcairo2-dev \
    && pip install pip==${PIP_VERSION} --no-cache-dir \
    && pip install uv==${UV_VERSION} --no-cache-dir \
    && mkdir -p '${APP_DIR}'\
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && apt-get clean -y && rm -rf /var/lib/apt/lists/*

WORKDIR ${APP_DIR}

RUN groupadd -g "${GROUPID}" -r ${RUNUSER} \
    && useradd -d '/data' -g ${RUNUSER} -l -r -u "${GROUPID}" ${RUNUSER} \
    && chown ${RUNUSER}:${RUNUSER} -R '/data'

# Copy only requirements, to cache them in docker layer
COPY --chown=${RUNUSER}:${RUNUSER} ./uv.lock ./pyproject.toml ${APP_DIR}/

# ----------------- Development stage -----------------
FROM base_build AS dev-runtime

RUN uv sync --all-extras --frozen \
  && chown ${RUNUSER}:${RUNUSER} -R '/data'

USER ${RUNUSER}

# ----------------- Runtime stage -----------------
FROM base_build AS prod-runtime

RUN uv sync --frozen \
  && chown ${RUNUSER}:${RUNUSER} -R '/data'

COPY src/ ${APP_DIR}/src
USER ${RUNUSER}
CMD ["/bin/bash"]