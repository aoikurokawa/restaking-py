import typing

from solders.pubkey import Pubkey

class Config:
    """
    The vault configuration account for the vault program.
    Manages program-wide settings and state.

    ...

    Attributes
    ----------
    admin : Pubkey
        The configuration admin

    restaking_program : Pubkey
        The approved restaking program for this vault
    
    epoch_length : int
        The length of an epoch in slots

    num_vaults: int
        The number of vaults managed by the program

    ncn_count : int
        The number of NCN managed by the program

    deposit_withdrawal_fee_cap_bps : int
        The fee cap in basis points ( withdraw and deposit )

    fee_rate_of_change_bps : int
        The maximum amount a fee can increase per epoch in basis points

    fee_bump_bps : int
        The amount a fee can increase above the rate of change in basis points

    program_fee_bps : int
        The program fee in basis points

    program_fee_wallet : Pubkey
        The fee wallet

    fee_admin : Pubkey
        The admin for the fee account

    bump : int
        The bump seed for the PDA


    Methods
    -------
    deserialize(data: bytes)
        Deserialize the account data to Config struct

    seeds():
        Returns the seeds for the PDA

    find_program_address(program_id: Pubkey):
        Find the program address for the Config account
    """

    discriminator: typing.ClassVar = 1

    admin: Pubkey
    restaking_program:Pubkey

    epoch_length: int
    num_vaults: int
    deposit_withdrawal_fee_cap_bps: int
    fee_rate_of_change_bps: int
    fee_bump_bps: int
    program_fee_bps: int

    program_fee_wallet: Pubkey
    fee_admin: Pubkey

    bump: int

    # Initialize a Config instance with required attributes
    def __init__(self, admin: Pubkey, restaking_program: Pubkey, epoch_length: int, num_vaults: int, deposit_withdrawal_fee_cap_bps: int, fee_rate_of_change_bps: int, fee_bump_bps: int, program_fee_bps: int, program_fee_wallet: Pubkey, fee_admin: Pubkey, bump: int):
        self.admin = admin
        self.restaking_program = restaking_program
        self.epoch_length = epoch_length
        self.num_vaults = num_vaults
        self.deposit_withdrawal_fee_cap_bps = deposit_withdrawal_fee_cap_bps
        self.fee_rate_of_change_bps = fee_rate_of_change_bps
        self.fee_bump_bps = fee_bump_bps
        self.program_fee_bps = program_fee_bps
        self.program_fee_wallet = program_fee_wallet
        self.fee_admin = fee_admin
        self.bump = bump

    @staticmethod
    def deserialize(data: bytes) -> "Config":
        """Deserializes bytes into a Config instance."""
        
        # Define offsets for each field
        offset = 0
        offset += 8

        # Admin
        admin = Pubkey.from_bytes(data[offset:offset + 32])
        offset += 32

        # Restaking Program
        restaking_program = Pubkey.from_bytes(data[offset:offset + 32])
        offset += 32

        # Epoch Length
        epoch_length = int.from_bytes(data[offset:offset + 8], byteorder='little')
        offset += 8

        # Number of Vaults
        num_vaults = int.from_bytes(data[offset:offset + 8], byteorder='little')
        offset += 8

        # Deposit Withdrawal Fee Cap BPS
        deposit_withdrawal_fee_cap_bps = int.from_bytes(data[offset:offset + 2], byteorder='little')
        offset += 2

        # Fee Rate of Change BPS
        fee_rate_of_change_bps = int.from_bytes(data[offset:offset + 2], byteorder='little')
        offset += 2

        # Fee Bump BPS
        fee_bump_bps = int.from_bytes(data[offset:offset + 2], byteorder='little')
        offset += 2

        # Program Fee BPS
        program_fee_bps = int.from_bytes(data[offset:offset + 2], byteorder='little')
        offset += 2

        # Program Fee Wallet
        program_fee_wallet = Pubkey.from_bytes(data[offset:offset + 32])
        offset += 32

        # Fee Admin
        fee_admin = Pubkey.from_bytes(data[offset:offset + 32])
        offset += 32
        
        # Bump
        bump = int.from_bytes(data[offset:offset + 1])

        # Return a new Config instance with the deserialized data
        return Config(
            admin=admin,
            restaking_program=restaking_program,
            epoch_length=epoch_length,
            num_vaults=num_vaults,
            deposit_withdrawal_fee_cap_bps=deposit_withdrawal_fee_cap_bps,
            fee_rate_of_change_bps=fee_rate_of_change_bps,
            fee_bump_bps=fee_bump_bps,
            program_fee_bps=program_fee_bps,
            program_fee_wallet=program_fee_wallet,
            fee_admin=fee_admin,
            bump=bump
        )

    @staticmethod
    def seeds() -> typing.List[bytes]:
        """Return the seeds used for generating PDA."""
        return [b"config"]
    
    @staticmethod
    def find_program_address(program_id: Pubkey) -> typing.Tuple[Pubkey, int, typing.List[bytes]]:
        """Finds the program-derived address (PDA) for the given seeds and program ID."""
        seeds = Config.seeds()
        
        # Compute PDA and bump using seeds (requires solders Pubkey functionality)
        pda, bump = Pubkey.find_program_address(seeds, program_id)
        
        return pda, bump, seeds

    # Display Config
    def __str__(self):
        return (
            f"Config(\n"
            f"  admin={self.admin},\n"
            f"  restaking_program={self.restaking_program},\n"
            f"  epoch_length={self.epoch_length},\n"
            f"  num_vaults={self.num_vaults},\n"
            f"  deposit_withdrawal_fee_cap_bps={self.deposit_withdrawal_fee_cap_bps},\n"
            f"  fee_rate_of_change_bps={self.fee_rate_of_change_bps},\n"
            f"  fee_bump_bps={self.fee_bump_bps},\n"
            f"  program_fee_bps={self.program_fee_bps},\n"
            f"  program_fee_wallet={self.program_fee_wallet},\n"
            f"  fee_admin={self.fee_admin},\n"
            f"  bump={self.bump},\n"
            f")"
        )
