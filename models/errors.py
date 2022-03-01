from enum import Enum

class FELError(Enum):
    IVAIncorrectamenteCalculado = 1
    FechaEmisionMayorAFechaCertificacion = 2
    NITNOEnRTU = 3
    NITNOAfiliadoIVA = 4
    EstablecimientoNoActivo = 5
    ValidacionTipoEspecial = 6
    PrecioIncorrecto = 7
    DescuentoExcesivo = 8
    ImpuestoIncorrectoTipoDTE = 9
    FraseNoRequeridaParaDTE = 10