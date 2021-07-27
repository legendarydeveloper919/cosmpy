from abc import ABC, abstractmethod
from cosmos.bank.v1beta1.query_pb2 import (
    QueryBalanceRequest,
    QueryBalanceResponse,
    QueryAllBalancesRequest,
    QueryAllBalancesResponse,
    QueryTotalSupplyRequest,
    QueryTotalSupplyResponse,
    QuerySupplyOfRequest,
    QuerySupplyOfResponse,
    QueryParamsRequest,
    QueryParamsResponse,
    QueryDenomMetadataRequest,
    QueryDenomsMetadataResponse,
    QueryDenomMetadataResponse,
    QueryDenomsMetadataRequest,
)


class Bank(ABC):
    @abstractmethod
    def Balance(self, request: QueryBalanceRequest) -> QueryBalanceResponse:
        """
        Queries balance of selected denomination from specific account

        :param request: QueryBalanceRequest with address and denomination

        :return: QueryBalanceResponse
        """
        pass

    @abstractmethod
    def AllBalances(self, request: QueryAllBalancesRequest) -> QueryAllBalancesResponse:
        """
        Queries balance of all denominations from specific account

        :param request: QueryAllBalancesRequest with account address

        :return: QueryAllBalancesResponse
        """
        pass

    @abstractmethod
    def TotalSupply(self, request: QueryTotalSupplyRequest) -> QueryTotalSupplyResponse:
        """
        Queries total supply of all denominations

        :param request: QueryTotalSupplyRequest

        :return: QueryTotalSupplyResponse
        """
        pass

    @abstractmethod
    def SupplyOf(self, request: QuerySupplyOfRequest) -> QuerySupplyOfResponse:
        """
        Queries total supply of specific denomination

        :param request: QuerySupplyOfRequest with denomination

        :return: QuerySupplyOfResponse
        """
        pass

    @abstractmethod
    def Params(self, request: QueryParamsRequest) -> QueryParamsResponse:
        """
        Queries the parameters of bank module

        :param request: QueryParamsRequest

        :return: QueryParamsResponse
        """
        pass

    @abstractmethod
    def DenomMetadata(
        self, request: QueryDenomMetadataRequest
    ) -> QueryDenomMetadataResponse:
        """
        Queries the client metadata for all registered coin denominations

        :param request: QueryDenomMetadataRequest with denomination

        :return: QueryDenomMetadataResponse
        """
        pass

    @abstractmethod
    def DenomsMetadata(
        self, request: QueryDenomsMetadataRequest
    ) -> QueryDenomsMetadataResponse:
        """
        Queries the client metadata of a given coin denomination

        :param request: QueryDenomsMetadataRequest

        :return: QueryDenomsMetadataResponse
        """
        pass
